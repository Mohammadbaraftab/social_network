from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth import get_user_model
from.models import Friendship
from django.db.models import Q

from .serializer import UserListSerializer

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.filter(is_superuser = False, is_staff = False, is_active = True)
        serializer = UserListSerializer(instance = users, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get("user")
        try:
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return Response({"message":"user dose not exitst"}, status=status.HTTP_400_BAD_REQUEST)
        Friendship.objects.get_or_create(request_from = request.user, request_to = user)
        return Response({"message":"request sent successfully."}, status=status.HTTP_201_CREATED)
    

class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendships = Friendship.objects.filter(request_to = request.user, is_accepted = False)
        users = set(case.request_from for case in friendships)
        serializer = UserListSerializer(instance = users, many = True)
        return Response(serializer.data)
    

class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get("user")
        try:
            user = User.objects.get(pk = user_id)
            friendship = Friendship.objects.get(request_to = request.user, 
                                                request_from = user, is_accepted = False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response({"message":"user or friendship dose not exist."}, 
                                                    status=status.HTTP_404_NOT_FOUND)
        friendship.is_accepted = True
        friendship.save()
        return Response({"message":"connected"}, status=status.HTTP_200_OK)
        

class FriendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        friendships = Friendship.objects.filter(
            Q(request_from=request.user) | Q(request_to=request.user),
            is_accepted=True
        ).select_related('request_from', 'request_to') 

        friends = set(
            friendship.request_from if friendship.request_to == request.user else friendship.request_to
            for friendship in friendships
        )

        serializer = UserListSerializer(instance=friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# class FriendView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):

#         friendships = Friendship.objects.filter(
#             Q(request_from=request.user) | Q(request_to=request.user),
#             is_accepted=True
#         ).select_related('request_from', 'request_to')  
#         friends_ids = {
#             friendship.request_from.id if friendship.request_to == request.user else friendship.request_to.id 
#             for friendship in friendships
#         }
#         friends = User.objects.filter(id__in=friends_ids)
#         serializer = UserListSerializer(instance=friends, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
