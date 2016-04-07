from django.db import models
from django.db.models import Q


# 自定义Manger
class MyPostManager(models.Manager):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)

    def get_raw_followers(self, user_login):
        """
        操作对象为Follow表
        获取所有的关注者，返回的是User对象构成的QuerySet,注意还需使用map将user2解析出来
        """
        return self.get_query_set().get_raw_followers(user_login)

    def get_raw_follows(self, user_login):
        """
        参照上
        """
        return self.get_query_set().get_raw_follows(user_login)

    # 操作对象为Post表
    # 根据提供的user列表，返回这些用户的posts，包含登录用户自己发布的
    def get_posts(self, user_login, follow_list):
        return self.get_query_set().get_posts(user_login, follow_list).order_by('-created_at')


class PostQuerySet(models.query.QuerySet):
    def get_raw_followers(self, user_login):
        return self.filter(user2=user_login)

    def get_raw_follows(self, user_login):
        return self.filter(user1=user_login)

    def get_posts(self, user_login, follow_list):
        return self.filter(Q(user=user_login) | Q(user__in=follow_list))

