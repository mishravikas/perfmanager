from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'perfmanager.views.index'),
    url(r'^alertsbyrev$', 'perfmanager.views.alertsbyrev'),
    url(r'^mergedalerts$', 'perfmanager.views.mergedalerts'),
    url(r'^updatefields$', 'perfmanager.views.updatefields'),
    url(r'^rev/(?P<keyrev>.+?)$', 'perfmanager.views.revision'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('accounts.urls')),
    (r'', include('django_browserid.urls')),
)
