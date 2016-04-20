import re
import base64
import datetime
from django.views.generic.base import TemplateView
from django.core.files.base import ContentFile
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
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
def index(request):
    u_login = get_user(request)

    visits = request.session.get('visits')
    last_visit_at = request.session.get('last_visit_at')
    reset_last_visit_time = False

    today = datetime.date.today()
    
    if not visits or not last_visit_at:
        visits = u_login.userprofile.visits
        last_visit_at = str(today)
        reset_last_visit_time = True

    last_visit_date = datetime.datetime.strptime(last_visit_at, "%Y-%m-%d").date()

    delta_days = (today - last_visit_date).days
    if delta_days == 1:
        visits += 1
        reset_last_visit_time = True
    if delta_days > 1:
        visits = 1
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit_at'] = str(datetime.date.today())
        request.session['visits'] = visits
        u_login.userprofile.visits = visits
        u_login.userprofile.save()

    return redirect('/{}/'.format(u_login.username))


@login_required
def homepage(request, user_name=None, current_page_num=1):
    """
    Homepage
    """
    current_page_num = int(current_page_num)
    context_dict = {}

    u_login = get_user(request)
    context_dict['u_login'] = u_login

    if user_name is None:
        user_of_this_page = u_login
    else:
        user_of_this_page = get_object_or_404(User, username=user_name)
    context_dict['user_of_this_page'] = user_of_this_page

    user_followers = Follow.my_post_manager.get_followers(user_of_this_page)
    all_posts = Post.my_post_manager.get_posts(user_of_this_page, user_followers).select_related('user__userprofile')
    
    context_dict['all_posts'] = myPaginatior(all_posts, 5, current_page_num)
    context_dict['posts_num'] = len(all_posts)

    if u_login.is_authenticated:
        context_dict['all_my_likes'] = [like.to.id for like in Like.objects.filter(by=u_login).select_related('to')]
        context_dict['all_my_comments'] = [comment.to.id for comment in Comment.objects.filter(by=u_login).select_related('to')]
    
    return render(request, 'index/homepage.html', context_dict)


@login_required
def query_cat(request, user_name=None):
    context_dict = {}

    u_login = get_user(request)
    context_dict['u_login'] = u_login
    user_of_this_page = get_object_or_404(User, username=user_name)
    context_dict['user_of_this_page'] = user_of_this_page

    def query(cat):
        return {
            'posts': Post.objects.filter(user=user_of_this_page),
            'followers': Follow.my_post_manager.get_followers(user_of_this_page),
            'follows': Follow.my_post_manager.get_follows(user_of_this_page)
        }.get(cat, redirect('/'))

    if request.method == 'GET':
        cat = request.GET['cat']
        context_dict['cat'] = cat
        context_dict['query_items'] = query(cat)
        return render(request, 'information_list/query_cat.html', context_dict)


@login_required
def get_comments(request):
    context_dict = {}
    if request.method == 'GET':
        post_id = request.GET['post_id']
        context_dict['post_id'] = post_id
        which_post = get_object_or_404(Post, id=int(post_id))
        comments_of_this_post = Comment.objects.filter(to=which_post).select_related('by', 'to__user', 'reply_to')
        context_dict['comments_of_this_post'] = myPaginatior(comments_of_this_post, 5, 1)

        return render(request, 'index/center/comments.html', context_dict)


@login_required
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
        
            Comment.objects.get_or_create(by=commented_by, to=comment_to, reply_to=comment_reply_to, content=comment_content)

            return redirect('/')


@login_required
def delete_comment(request):
    comments_num = 0
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        post_id = request.GET['post_id']

        if comment_id:
            comment = get_object_or_None(Comment, id=comment_id)
            comment.delete()

            post = get_object_or_None(Post, id=post_id)
            comments_num = Comment.objects.filter(to=post).count()
        
        return HttpResponse(comments_num)


@login_required
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


@login_required
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


@login_required
def follow_sb(request):
    resp = {'text': '关注', 'code': '0'}
    
    if request.method == 'GET':

        user2_id = request.GET['user2_id']

        if user2_id:
            user1 = get_user(request)
            user2 = get_object_or_None(User, id=user2_id)

            if user1 and user2:
                obj, created = Follow.objects.get_or_create(user1=user1, user2=user2)
                if not created:
                    obj.delete()
                    resp['code'] = '0'
                else:
                    if obj.situation == '1':
                        resp['text'] = '相互关注'
                    else:
                        resp['text'] = '已关注'
                    resp['code'] = obj.situation

        return JsonResponse(resp)


@login_required
def my_page(request, user_name=None):
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
        return redirect('/{}/my_page/'.format(u_login.username))
    return render(request, 'people/people.html', context_dict)


@login_required
def set_portrait(request):
    u_login = get_user(request)
    if request.method == 'POST':
        raw_img = request.POST['image_data'].partition('base64,')[2]
        up_obj, created = UserProfile.objects.get_or_create(user=u_login)
        img = base64.b64decode(raw_img)
        up_obj.portrait.save('user.jpg', ContentFile(img), save=True)
    return HttpResponse(up_obj.portrait.url)


class AboutMeView(TemplateView):
    template_name = 'about_me.html'

class CanvasDemoView(TemplateView):
    template_name = 'canvas.html'
