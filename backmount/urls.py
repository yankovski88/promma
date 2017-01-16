# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from backmount.views import backmount

urlpatterns = patterns('',
                url(r'backmount/$', backmount),
)
