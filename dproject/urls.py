from django.conf.urls import patterns, url
from dproject import views

urlpatterns = patterns('',
    # top site level
    url(r'^$', views.index, name='index'),
    # about page
    url(r'^about/$', views.about, name='about'),
    # check URL, cleanup, and redirect to indexvids
    url(r'youtube.com/(?P<vidId>.+)/$', views.indexvidsurl, name='indexvidsurl'),
    # set timing of submitted transcript
    # url(r'youtube.com/(?P<vidId>.+)/timing/$', views.set_vid_timing, name='set_vid_timing'),
    # main vid viewing and transcripts
    url(r'^(?P<vidId>.{11})/', views.indexvids, name='indexvids'),
    # holder for form submit
    url(r'^transcript_submit/(?P<vidId>.+)/$', views.transcript_submit, name='transcript_submit'),
    # not sure if still active
    url(r'^video_search_request/(?P<searchInput>.+)/$', views.video_search_submit, name='video_search_submit'),
    # 404 redirect to top site level
    url(r'^.+/$', views.notfound, name='redirect')
    # note: need Python or JavaScript to prevent live pages views with empty YT
    # vids. host/asdf/asdf gives this kid of "ghost" page.
)
