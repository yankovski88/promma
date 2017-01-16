# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from pb.views import pb

urlpatterns = patterns('',
                       url (r'^$', pb),
                       )
