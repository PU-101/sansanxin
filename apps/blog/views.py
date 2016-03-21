from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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

    all_comments = Comment.objects.all()
    context_dict['all_comments'] = all_comments

    return render(request, 'base.html', context_dict)


def get_comments(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        which_post = get_object_or_404(Post, id=int(post_id))
        comments_of_this_post = Comment.objects.filter(post=which_post)
        
        return render(request, 'center/comments.html', {'comments_of_this_post': comments_of_this_post})


def post_comment(request):
    if request.method == 'POST':
        comment_by = get_user(request)
        post_id = request.POST['comment_to']
        # reply_to = request.POST['reply_to']
        comment_content = request.POST['comment_content']
        comment_to = get_object_or_404(Post, id=post_id)
        c = Comment.objects.create(post=comment_to, user=comment_by, content=comment_content)

        return redirect('/')

