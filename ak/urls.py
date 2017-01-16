# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from ak.views import ak

urlpatterns = patterns('',
                       url (r'^$', ak),
                       )
