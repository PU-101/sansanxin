from django.db.models import Q
from django import template 
from operator import itemgetter
from django.contrib.auth.models import User
from apps.blog.views import get_object_or_None
from apps.blog.models import UserProfile, Post, Like, Follow, Comment
from apps.spider.models import Calendar
from apps.blog.forms import PostForm

register = template.Library()


@register.inclusion_tag('index/left/profile.html')
def get_userprofile_info(u_login, user_of_this_page):
    user_prof = get_object_or_None(UserProfile, user=user_of_this_page)
    context_dict = {'user': u_login, 'user_of_this_page': user_of_this_page, 'user_prof': user_prof}

    if u_login == user_of_this_page:
        context_dict['situation'] = 'hidden'
    else:
        obj = Follow.objects.filter(user1=u_login, user2=user_of_this_page)
        if obj:
            context_dict['situation'] = obj[0].situation
        else:
            context_dict['situation'] = 'new'

    return context_dict


@register.inclusion_tag('index/right/calendars.html')
def get_mafengwo_list():
    return {'cals': Calendar.objects.all()[:10]}


@register.inclusion_tag('index/center/post_form.html')
def create_post_form():
    form = PostForm()
    return {'post_form': form}


@register.inclusion_tag('people/activity.html')
def get_activities_list(user_login):
    activities_list = []

    posts = Post.objects.filter(user=user_login)
    posts_list = ({'post': post, 'created_at': post.created_at} for post in posts)
    activities_list.extend(posts_list)

    likes = Like.objects.filter(by=user_login).select_related('to')
    likes_list = ({'like': like, 'created_at': like.created_at} for like in likes)
    activities_list.extend(likes_list)

    comments = Comment.objects.filter(by=user_login).select_related('to')
    comments_list = ({'comment': comment, 'created_at': comment.created_at} for comment in comments)
    activities_list.extend(comments_list)

    follows = Follow.objects.filter(user1=user_login).select_related('user2')
    follows_list = ({'follow': follow, 'created_at': follow.created_at} for follow in follows)
    activities_list.extend(follows_list)

    followers = Follow.objects.filter(user2=user_login).select_related('user1')
    followers_list = ({'follower': follower, 'created_at': follower.created_at} for follower in followers)
    activities_list.extend(followers_list)
    
    activities_list = sorted(activities_list, key=itemgetter('created_at'), reverse=True)
    return {'activities_list': activities_list}


@register.inclusion_tag('index/left/about.html')
def get_interested_people(u_login):
    follows_list = Follow.my_post_manager.get_follows(u_login)
    follows_name = (follow.username for follow in follows_list)
    all_interested_people = User.objects.exclude(Q(username=u_login.username) | Q(username__in=follows_name)).select_related('userprofile')
    interested_people = all_interested_people.order_by('?')[:5]
    return {'u_login': u_login, 'interested_people': interested_people}
