from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, LikeSerializer, CommentSerializer

from .models import Post, Like


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            posts = Post.objects.filter(is_active = True, user = request.user)
        except Post.DoesNotExist:
            return Response({"error":"post not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(instance = posts, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response({"message": "Post created successfully.", "post": serializer.data}, 
                                           status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return False

    def get(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        # comments = Comment.objects.filter(post=post, is_approved=True)
        comments = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_pk):
        post = self.get_post(post_pk)
        if not post:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response({"message": "Comment created successfully.", "comment": serializer.data},
                                         status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Post.objects.get(pk = post_id)
        except Post.DoesNotExist:
            return False
        
    def get(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        likes = post.likes.filter(is_like = True).count()
        return Response({"message": "Like status updated.", "like": likes}, status=status.HTTP_200_OK) 
    
    def post(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response({"massage":"post not found"}, status=status.HTTP_404_NOT_FOUND)
        serilizer = LikeSerializer(data = request.data)
        if serilizer.is_valid(raise_exception=True):
            serilizer.save(post = post, user = request.user)
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)





# class LikeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, post_pk):
#         try:
#             post = Post.objects.get(id=post_pk)
#         except Post.DoesNotExist:
#             return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

#         like, created = Like.objects.get_or_create(post=post, user=request.user)

#         if not created: 
#             like.is_like = not like.is_like  
#             like.save()

#             serializer = LikeSerializer(instance = like)
#             return Response({"message": "Like status updated.", "like": serializer.data}, status=status.HTTP_200_OK)
        
#         serializer = LikeSerializer(instance = created)
#         return Response({"message": "Liked the post.", "like": serializer.data}, status=status.HTTP_201_CREATED)