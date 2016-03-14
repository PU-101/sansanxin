from django.contrib import admin
from .models import Like, Star, Follow


# Register your models here.
admin.site.register(Like)
admin.site.register(Star)
admin.site.register(Follow)