from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import autodata.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sgaosite.views.home', name='home'),
    # url(r'^sgaosite/', include('sgaosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#     url(r'', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # failed in apache + mod_python
    # url(r'^autodata/', include('autodata.urls')),
    url(r'^autodata/', include(autodata.urls)),
    # url(r'^add/', include('add.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }, name="media"),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
