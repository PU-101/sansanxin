from django.shortcuts import render
from django.db.models import Q


from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Post, Follow

# Create your views here.
class PostList(ListView):
	u = User.objects.get(username='lkl')
	my_follows = map(lambda x: x.user2, Follow.my_post_manager.get_raw_followers(u))

	queryset = my_follows

	template_name = 'index.html'
