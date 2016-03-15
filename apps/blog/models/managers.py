from django.db import models


class MyPostManager(models.Manager):
	def get_query_set(self):
		return PostQuerySet(self.model, using=self._db)

	def get_raw_followers(self, user_instance):
		return self.get_query_set().get_raw_followers(user_instance)


class PostQuerySet(models.query.QuerySet):
	def get_raw_followers(self, user_instance):
		return self.filter(user1=user_instance)
