from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('dproject.urls'), name='vidResponse'),
    #url(r'^$', include('dproject.urls'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
