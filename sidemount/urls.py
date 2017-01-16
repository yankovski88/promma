# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from sidemount.views import sidemount

urlpatterns = patterns('',
                       url (r'^sidemount/$', sidemount),
                       )
