from django.conf.urls import patterns, url
from dproject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<vidId>.+)/$', views.indexvids, name='indexvids'),
)
