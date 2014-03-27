from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # auth skip logout confirmation
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # auth
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^', include('dproject.urls'), name='index'),
)
