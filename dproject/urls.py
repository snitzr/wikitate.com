from django.conf.urls import patterns, url
from dproject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'youtube.com/(?P<vidId>.+)/$', views.indexvidsurl, name='indexvidsurl'),
    url(r'^(?P<vidId>.{11})/$', views.indexvids, name='indexvids'),
    url(r'^transcript_submit/(?P<vidId>.+)/$', views.transcript_submit, name='transcript_submit'),
    url(r'^video_search_request/(?P<searchInput>.+)/$', views.video_search_submit, name='video_search_submit'),
    url(r'^.+/$', views.notfound, name='redirect')
)
