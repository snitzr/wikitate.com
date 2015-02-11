from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # auth skip logout confirmation
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # auth
    url(r'^accounts/', include('allauth.urls'), name='accounts'),
    url(r'^accounts/profile/$', include('accounts.urls'), name='profile'),
    url(r'^', include('dproject.urls', namespace='index')),
)
