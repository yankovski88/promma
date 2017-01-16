# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from mount.views import mount

urlpatterns = patterns('',
                       url (r'^mount/$', mount),
                       )
