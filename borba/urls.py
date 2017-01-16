# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from borba.views import borba

urlpatterns = patterns('',
                       url (r'^$', borba),
                       )
