# -*- coding: utf-8 -*-

from django.conf.urls import  url, patterns
from yumor.views import  yumor_name, yumor_redirect, yumor_base

urlpatterns = patterns('',
    url(r'^$', yumor_base),
    url(r'^dobavit/$', yumor_name),
    url(r'^redirect/$', yumor_redirect),
                       )
