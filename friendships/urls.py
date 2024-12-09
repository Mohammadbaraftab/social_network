from .import views
from django.urls import path


app_name = "friendships"
urlpatterns = [
    path("user_list/", views.UserListView.as_view(), name="user_list"),
    path("request/", views.RequestView.as_view(), name="request"),
    path("request_list/", views.RequestListView.as_view(), name="request_list"),
    path("accept/", views.AcceptView.as_view(), name="accept"),
    path("friends/", views.FriendView.as_view(), name="friends"),
  ]