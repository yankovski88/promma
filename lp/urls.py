# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from lp.views import lp

urlpatterns = patterns('',
                       url (r'^$', lp),
                       )
