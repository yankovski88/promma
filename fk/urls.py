# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from fk.views import fk

urlpatterns = patterns('',
                       url (r'^$', fk),
                       )
