from django.contrib import admin 
from apps.blog.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')

admin.site.register(Comment, CommentAdmin)