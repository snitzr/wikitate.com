from django.conf.urls import patterns, url
from dproject import views

urlpatterns = patterns('',
    url(r'(?P<vid_id>)$', views.vidResponse, name='vidResponse'),
    # url(r'^$', views.index, name='index'),
)
