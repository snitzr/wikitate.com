from django.conf.urls import patterns, url
from dproject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'youtube.com/(?P<vidId>.+)/$', views.indexvids, name='indexvids'),
    url(r'^(?P<vidId>.{11})/$', views.indexvids, name='indexvids'),
    url(r'^.+/$', views.notfound, name='redirect'),
    #testing
    url(r'^/login/$', 'django.contrib.auth.views.login', {'template_name':                                                          'dproject/login.html'}),
)
