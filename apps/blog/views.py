import re
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import UserProfile, Post, Follow, Comment, Like
from .forms import CommentForm, PostForm, UserForm, UserProfileForm


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
    """
    Homepage
    """
    current_page_num = int(current_page_num)
    context_dict = {}

    u_login = get_user(request)

    user_follows = map(lambda x: x.user2, Follow.my_post_manager.get_raw_followers(u_login))
    all_posts = Post.my_post_manager.get_posts(u_login, user_follows).select_related('user')
    
    context_dict['all_posts'] = myPaginatior(all_posts, 10, current_page_num)

    context_dict['all_my_likes'] = [like.to.id for like in Like.objects.filter(by=u_login).select_related('to')]
    context_dict['all_my_comments'] = [comment.to.id for comment in Comment.objects.filter(by=u_login).select_related('to')]
    return render(request, 'index/index.html', context_dict)


def get_comments(request):
    context_dict = {}
    if request.method == 'GET':
        post_id = request.GET['post_id']
        context_dict['post_id'] = post_id
        which_post = get_object_or_404(Post, id=int(post_id))
        comments_of_this_post = Comment.objects.filter(to=which_post).select_related('by', 'to__user', 'reply_to')
        context_dict['comments_of_this_post'] = myPaginatior(comments_of_this_post, 5, 1)

        return render(request, 'index/center/comments.html', context_dict)


def post_comment(request):
    if request.method == 'POST':
        commented_by = get_user(request)
        post_id = request.POST['comment_to']
        comment_to = get_object_or_404(Post, id=post_id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment_raw_content = form.cleaned_data['comment_field']
            pattern = re.compile(r'^(?:\s*回复\s*(.*?)\s*[:：]+)?\s*(.*?)$')
            comment_reply_to, comment_content = re.match(pattern, comment_raw_content).groups()

            try:
                comment_reply_to = get_object_or_None(User, username=comment_reply_to)
            except User.DoesNotExist:
                comment_reply_to = None
        
            obj, created = Comment.objects.get_or_create(by=commented_by, to=comment_to, reply_to=comment_reply_to, content=comment_content)

            return redirect('/')


def delete_comment(request):
    if request.method == 'GET':
        comment_id = request.GET['comment_id']

        if comment_id:
            comment = get_object_or_None(Comment, id=comment_id)
            comment.delete()
        
        return HttpResponse(None)


def post_postitem(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.user = get_user(request)
            # if 'picture' in request.FILES:
            #     form.picture = request.FILES['picture']
            form.save()

        return redirect('/')


def like_post(request):
    likes_num = 0
    if request.method == 'GET':
        post_id = request.GET['post_id']
        user_id = request.GET['user_id']

        if post_id and user_id:
            post = get_object_or_None(Post, id=post_id)
            user = get_object_or_None(User, id=user_id)

            if post and user:
                obj, created = Like.objects.get_or_create(by=user, to=post)
                if not created:
                    obj.delete()
                likes_num = Post.objects.get(id=post_id).likes_num

        return HttpResponse(likes_num)


def profile(request):
    context_dict = {}
    u_login = get_user(request)
    up_obj, created = UserProfile.objects.get_or_create(user=u_login)

    user_form = UserForm(request.POST or None, instance=u_login)
    userprof_form = UserProfileForm(request.POST or None, request.FILES or None, instance=up_obj)
    context_dict['user_form'] = user_form
    context_dict['userprof_form'] = userprof_form

    if request.method == 'POST':
        if user_form.is_valid() and userprof_form.is_valid():
            user_form.save()
            userprof_form.save()
        return redirect('/my_page/')
    return render(request, 'people/people.html', context_dict)


def set_portrait(request):
    if request.method == 'POST':
        img = request.POST['image_data']
        print(img)
    return HttpResponse('haha')
