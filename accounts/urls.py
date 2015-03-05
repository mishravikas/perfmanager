from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^profile/$', 'accounts.views.profile'),
    # url(r'^blog/', include('blog.urls')),

)
