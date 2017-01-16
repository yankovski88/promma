# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from lo.views import lo

urlpatterns = patterns('',
                       url (r'^$', lo),
                       )
