# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from pp.views import pp

urlpatterns = patterns('',
                       url (r'^$', pp),
                       )
