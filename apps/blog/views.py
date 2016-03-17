from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import UserProfile, Post, Follow, Comment


# Create your views here.
# class PostList(ListView):
#     u = User.objects.get(username='lkl')
#     my_follows = map(lambda x: x.user2, Follow.my_post_manager.get_raw_followers(u))
#     my_follows_posts = Post.my_post_manager.get_posts(u, my_follows)

#     queryset = my_follows_posts

#     template_name = 'base.html'


@login_required
def index(request):
	context_dict = {}

	u_login = get_user(request)
	user_prof = get_object_or_404(UserProfile, user=u_login)
	context_dict['user_prof'] = user_prof

	user_follows = map(lambda x: x.user2, Follow.my_post_manager.get_raw_followers(u_login))
	all_posts = Post.my_post_manager.get_posts(u_login, user_follows)
	context_dict['all_posts'] = all_posts

	return render(request, 'base.html', context_dict)


