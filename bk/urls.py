# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from bk.views import bk

urlpatterns = patterns('',
                       url (r'^$', bk),
                       )
