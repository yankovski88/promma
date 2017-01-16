# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from hk.views import hk

urlpatterns = patterns('',
                       url (r'^$', hk),
                       )
