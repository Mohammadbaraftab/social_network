from django.contrib import admin
from .models import Post, PostFile, Comment, Like


class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile  
    fields = ("post", "file")
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "is_active", "created_time")
    list_filter = ("title", "is_active")
    inlines = [PostFileInlineAdmin,]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "is_approved", "created_time")
    list_filter = ("is_approved", "created_time")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "is_like", "created_time")
    list_filter = ("is_like", "created_time")