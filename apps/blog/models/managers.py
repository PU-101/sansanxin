from django.db import models
from django.db.models import Q


# 自定义Manger
class MyPostManager(models.Manager):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)

    # 获取所有的关注者，返回的是User对象构成的QuerySet
    def get_raw_followers(self, user_instance):
        return self.get_query_set().get_raw_followers(user_instance)

    # 根据提供的user列表，返回这些用户的posts，包含登录用户自己的状态
    def get_posts(self, user_login, user_list):
        return self.get_query_set().get_posts(user_login, user_list).order_by('-created_at')


class PostQuerySet(models.query.QuerySet):
    def get_raw_followers(self, user_instance):
        return self.filter(user1=user_instance)

    def get_posts(self, user_login, user_list):
        return self.filter(Q(user__in=user_list) | Q(user=user_login))

