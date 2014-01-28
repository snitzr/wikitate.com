from django.conf.urls import patterns, url

from subtext import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
