from django.contrib import admin
from apps.blog.models import Like, Follow


class FollowAdmin(admin.ModelAdmin):
	fields = ('user1', 'situation', 'user2')


# Register your models here.
admin.site.register(Like)
admin.site.register(Follow, FollowAdmin)