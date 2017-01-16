# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from lk.views import lk

urlpatterns = patterns('',
                       url (r'^$', lk),
                       )
