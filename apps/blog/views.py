import re
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import UserProfile, Post, Follow, Comment
from .forms import CommentForm



def get_object_or_None(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist and model.MultipleObjectsReturned:
        return None


def myPaginatior(obj_list, per_page=10, current_page_num=1):
    paginator = Paginator(obj_list, per_page)
    page_range = paginator.page_range
    try:
        context = paginator.page(current_page_num)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)
    finally:
        setattr(context, 'page_range', page_range)
        return context


@login_required
def index(request, current_page_num=1):
    current_page_num = int(current_page_num)
    context_dict = {}

    u_login = get_user(request)
    # user_prof = get_object_or_404(UserProfile, user=u_login)
    # context_dict['user_prof'] = user_prof

    user_follows = map(lambda x: x.user2, Follow.my_post_manager.get_raw_followers(u_login))
    all_posts = Post.my_post_manager.get_posts(u_login, user_follows).select_related('user')
    
    context_dict['all_posts'] = myPaginatior(all_posts, 3, current_page_num)

    return render(request, 'base.html', context_dict)


def get_comments(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        which_post = get_object_or_404(Post, id=int(post_id))
        comments_of_this_post = Comment.objects.filter(to=which_post).select_related('by', 'to__user', 'reply_to')
        comments_of_this_post = myPaginatior(comments_of_this_post, 5, 1)

        return render(request, 'center/comments.html', {'comments_of_this_post': comments_of_this_post, 'post_id': post_id})


def post_comment(request):
    if request.method == 'POST':
        commented_by = get_user(request)
        post_id = request.POST['comment_to']
        comment_to = get_object_or_404(Post, id=post_id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment_raw_content = form.cleaned_data['comment_field']
            print('-----------------------------------')
            print(comment_raw_content.encode('utf8mb4'))
            pattern = re.compile(r'^(?:\s*回复\s*(.*?)\s*[:：]+)?\s*(.*?)$')
            comment_reply_to, comment_content = re.match(pattern, comment_raw_content).groups()
            print(comment_reply_to, comment_content)

            try:
                comment_reply_to = get_object_or_None(User, username=comment_reply_to)
            except User.DoesNotExist:
                comment_reply_to = None
        
            c = Comment.objects.create(by=commented_by, to=comment_to, reply_to=comment_reply_to, content=comment_content)

        return redirect('/')

