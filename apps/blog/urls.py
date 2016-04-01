from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^(?P<current_page_num>\d+)/$', views.index, name='pagination_page'),
    url(r'^comments/get_comments/$', views.get_comments, name='get_comments'),
    url(r'^comments/post_comment/$', views.post_comment, name='post_comment'),

    url(r'^posts/post_postitem/$', views.post_postitem, name='post_postitem'),

]