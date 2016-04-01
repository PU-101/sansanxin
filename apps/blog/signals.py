from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from django.contrib.auth.models import User
from apps.blog.models import UserProfile, Follow, Comment


# @receiver(post_save, sender=User)
# def create_profile_handler(sender, instance, created, **kwargs):
#     if not created:
#         return
#     profile = UserProfile(user=instance)
#     profile.save()


# @receiver(post_save, sender=Follow)
# def add_follow(sender, instance, created, **kwargs):
#     # if not created:
#     #     return
#     print('------------------------')
#     u1 = instance.user1
#     u2 = instance.user2
#     u1.update(follows=F('follows') + 1)
#     u2.update(follows=F('follows') + 1)


# def add_or_cancle_comment(delta):
#     """
#     在Comment表保存后修改Post中的comment_num字段数目
#     """
#     def f(instance, **kwargs):
#         to_post = instance.to
#         to_post.comments_num = F('comments_num') + delta
#         to_post.save()
#     return f

# post_save.connect(add_or_cancle_comment(1), sender=Comment)
# post_delete.connect(add_or_cancle_comment(-1), sender=Comment)