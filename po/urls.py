# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from po.views import po

urlpatterns = patterns('',
                       url (r'^$', po),
                       )
