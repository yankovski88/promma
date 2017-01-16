# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from udsr.views import udsr

urlpatterns = patterns('',
                       url (r'^$', udsr),
                       )
