from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from accounts import views
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^accounts/profile/$', views.profile, name='profile'),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^$', TemplateView.as_view(template_name='index.html')),
                       url(r'^admin/', include(admin.site.urls)),
)
