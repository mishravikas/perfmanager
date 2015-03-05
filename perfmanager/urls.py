from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'perfmanager.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('accounts.urls')),
    (r'', include('django_browserid.urls')),
)
