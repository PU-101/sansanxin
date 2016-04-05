from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index, name='spider'),
    url(r'^destination/$', views.get_destination_list, name='destination'),

]