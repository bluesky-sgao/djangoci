from django.conf.urls.defaults import *
from autodata.views import autodata

urlpatterns = patterns('',
    url(r'^$', autodata),
)
