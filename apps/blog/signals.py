from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from django.contrib.auth.models import User
# from models import UserProfile, Follow


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