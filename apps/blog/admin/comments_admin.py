from django.contrib import admin 
from apps.blog.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('to', 'by', 'content', 'created_at')

admin.site.register(Comment, CommentAdmin)