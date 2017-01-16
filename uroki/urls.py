# -*- coding: utf-8 -*-

from django.conf.urls import  url, patterns
from uroki.views import  uroki

urlpatterns = patterns('',
    url(r'^$', uroki),
                       )