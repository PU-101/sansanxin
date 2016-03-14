from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile


# Register your models here.
class UserProfileInline(admin.TabularInline):
	model = UserProfile
	extra = 1


class UserAdmin(admin.ModelAdmin):
	inlines = [UserProfileInline, ]
	list_display = ('username', 'email', 'create_at', 'is_staff')
	fields = ('username', 'password', 'email')

	def create_at(self, obj):
		return obj.userprofile.created_at.strftime('%Y-%m-%d %H:%M:%S')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)