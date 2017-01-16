# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from lb.views import lb

urlpatterns = patterns('',
                       url (r'^$', lb),
                       )
