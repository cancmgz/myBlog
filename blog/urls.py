from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^page/(?P<pk>\d+)/$', views.pageDetail, name='pageDetail'),
    url(r'^home/$', views.index, name='home'),
    url(r'^home/(?P<pageNumber>\w{0,50})/$', views.index, name='home'),
    url(r'^photo/$', views.photo, name='photo')
]