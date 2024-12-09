from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2048)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['title', 'is_active']

    def __str__(self):
        return self.title
    

class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_files")
    file = models.FileField(blank=True, null=True, upload_to="file/")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "postfile"
        verbose_name = "PostFile"
        verbose_name_plural = "PostFiles"


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return f"{self.user} commented on {self.post}"


class ReplyComment(models.Model):
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reply_comment"
        verbose_name = "Reply Comment"
        verbose_name_plural = "Reply Comments"

    def __str__(self) -> str:
        return f"{self.user} replied to {self.comment}"
    

class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    is_like = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "like"
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self) -> str:
        return f"{self.user} {'liked' if self.is_like else 'disliked'} {self.post}"
