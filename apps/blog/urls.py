from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^(?P<current_page_num>\d+)/$', views.index, name='pagination_page'),
    url(r'^comments/get_comments/$', views.get_comments, name='get_comments'),
    url(r'^comments/post_comment/$', views.post_comment, name='post_comment'),
    url(r'^comments/delete_comment/$', views.delete_comment, name='delete_comment'),


    url(r'^posts/post_postitem/$', views.post_postitem, name='post_postitem'),
    url(r'^posts/like_post/$', views.like_post, name='like_post'),

    url(r'^my_page/$', views.profile, name='my_page'),

]