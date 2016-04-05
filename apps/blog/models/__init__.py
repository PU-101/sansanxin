from .managers import MyPostManager
from .posts import Post
from .users import UserProfile
from .relationship import Like, Follow
from .comments import Comment

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import F


"""
－－－－－－SIGNALS－－－－－－－
"""


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    """
    创建用户的同时，创建对应的UserProfile表
    """
    if not created:
        return
    UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Post)
def count_posts(sender, instance, created, **kwargs):
    if not created:
        return
    by = instance.user
    posts_num = Post.objects.filter(user=by).count()
    UserProfile.objects.filter(user=by).update(posts_num=posts_num)


def count_likes(instance):
    to_post = instance.to
    likes_num = Like.objects.filter(to=to_post).count()
    Post.objects.filter(id=to_post.id).update(likes_num=likes_num)
    

@receiver(post_save, sender=Like)
def add_like(sender, instance, created, **kwargs):
    if not created:
        return
    count_likes(instance)


@receiver(post_delete, sender=Like)
def cancle_like(sender, instance, **kwargs):
    count_likes(instance)


def count_comments(instance):
    to_post = instance.to
    comments_num = Comment.objects.filter(to=to_post).count()
    Post.objects.filter(id=to_post.id).update(comments_num=comments_num)


@receiver(post_save, sender=Comment)
def add_comment(sender, instance, created, **kwargs):
    if not created:
        return
    count_comments(instance)


@receiver(post_delete, sender=Comment)
def cancle_comment(sender, instance, **kwargs):
    count_comments(instance)


def count_follows(instance):
    u1 = instance.user1
    u2 = instance.user2

    u1_follows_num = Follow.objects.filter(user1=u1).count()
    UserProfile.objects.filter(user=u1).update(follows_num=u1_follows_num)

    u2_followers_num = Follow.objects.filter(user2=u2).count()
    UserProfile.objects.filter(user=u2).update(followers_num=u2_followers_num)
    

@receiver(post_save, sender=Follow)
def add_follow(sender, instance, created, **kwargs):
    if not created:
        return
    count_follows(instance)


@receiver(post_delete, sender=Follow)
def cancle_follow(sender, instance, **kwargs):
    count_follows(instance)

