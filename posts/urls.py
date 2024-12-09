from .import views
from django.urls import path


app_name = "posts"
urlpatterns = [
    path("posts/", views.PostView.as_view(), name="post"),
    path('posts/<int:post_pk>/comments/', views.CommentView.as_view(), name='comment'),
    path('posts/<int:post_id>/likes/', views.LikeView.as_view(), name='like'),
]   