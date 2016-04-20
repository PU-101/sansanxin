from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^follow/$', views.follow_sb, name='follow_sb'),
    
    url(r'^comments/get_comments/$', views.get_comments, name='get_comments'),
    url(r'^comments/post_comment/$', views.post_comment, name='post_comment'),
    url(r'^comments/delete_comment/$', views.delete_comment, name='delete_comment'),

    url(r'^posts/post_postitem/$', views.post_postitem, name='post_postitem'),
    url(r'^posts/like_post/$', views.like_post, name='like_post'),

    url(r'^portrait/set_portrait/$', views.set_portrait, name='set_portrait'),

    url(r'^about_me/$', views.AboutMeView.as_view(), name='about_me'),

    url(r'^canvas_demo/', views.CanvasDemoView.as_view(), name='canvas_demo'),

    url(r'^(?P<user_name>\w+)/$', views.homepage, name='homepage'),
    url(r'^(?P<user_name>\w+)/(?P<current_page_num>\d+)/$', views.homepage, name='pagination_page'),
    url(r'^(?P<user_name>\w+)/my_page/$', views.my_page, name='my_page'),
    url(r'^(?P<user_name>\w+)/query/$', views.query_cat, name='query_cat'),
]