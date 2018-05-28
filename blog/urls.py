from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^home$', views.index, name='home'),
    url(r'^page/(?P<pk>\d+)/$', views.pageDetail, name='pageDetail')
]