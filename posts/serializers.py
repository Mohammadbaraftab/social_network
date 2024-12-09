from rest_framework import serializers

from.models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "user", "title", "content", "is_active", "is_public")
        extra_kwargs ={
            "user":{"read_only":True}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "user", "content", "is_approved")
        extra_kwargs = {
            "post":{"read_only":True},
            "user":{"read_only":True}, 
            "is_approved":{"required":False}
        }


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user', 'is_like')
        extra_kwargs = {
            "post":{"read_only":True},
            "user":{"read_only":True},
            "is_like":{"required":False}
        }