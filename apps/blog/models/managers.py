from django.db import models
from django.db.models import Q


# 自定义Manger
class MyPostManager(models.Manager):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)

    def get_raw_followers(self, user):
        """
        操作对象为Follow表
        获取所有的关注者，返回的是User对象构成的QuerySet,注意还需使用map将user2解析出来,以及相应的关注情况
        """
        return self.get_query_set().get_raw_followers(user)

    def get_followers(self, user):
        raw_follow_list = self.get_raw_followers(user)
        map(lambda single: setattr(single.user1, 'situation', single.situation), raw_follow_list)
        return (single.user1 for single in raw_follow_list)
         
    def get_raw_follows(self, user):
        """
        参照上
        """
        return self.get_query_set().get_raw_follows(user)

    def get_follows(self, user):
        raw_follow_list = self.get_raw_follows(user)
        map(lambda single: setattr(single.user2, 'situation', single.situation), raw_follow_list)
        return (single.user2 for single in raw_follow_list)

    # 操作对象为Post表
    # 根据提供的user列表，返回这些用户的posts，包含登录用户自己发布的
    def get_posts(self, user, follow_list):
        return self.get_query_set().get_posts(user, follow_list).order_by('-created_at')


class PostQuerySet(models.query.QuerySet):
    def get_raw_followers(self, user):
        return self.filter(user2=user)

    def get_raw_follows(self, user):
        return self.filter(user1=user)

    def get_posts(self, user, follow_list):
        return self.filter(Q(user=user) | Q(user__in=follow_list))

