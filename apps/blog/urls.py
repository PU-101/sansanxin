from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comments/get_comments/$', views.get_comments, name='get_comments')
]