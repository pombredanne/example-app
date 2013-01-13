from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import compositeadmin


admin.autodiscover()
compositeadmin.site.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'delicatewebizen.views.home', name='home'),
    url(r'^', include('main.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compositeadmin/', compositeadmin.site.include_urls()),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
