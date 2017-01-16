# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
# проверка переноса

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'promma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

url (r'^us/', include ('us.urls')), # о нас
url (r'^$', include ('index.urls')), # это главная страница
url (r'^uroki/', include ('uroki.urls')), # в общем уроки
url (r'^lp/', include ('lp.urls')), # уроки на левый прямой
url (r'^pp/', include ('pp.urls')), # уроки на правый прямой
url (r'^pb/', include ('pb.urls')), # уроки на правый боковой
url (r'^lb/', include ('lb.urls')), # уроки на левый боковой
url (r'^lo/', include ('lo.urls')), # уроки на левый опперкот
url (r'^po/', include ('po.urls')), # уроки на правый опперкот
url (r'^bk/', include ('bk.urls')), # бэкфист
url (r'^yumor/', include ('yumor.urls')), # юмор главная
url (r'^dobavit/', include ('yumor.urls')), # юмор редирект
url (r'^lk/', include ('lk.urls')), # лоу кик
url (r'^udsr/', include ('udsr.urls')), # прямой удар с разворота
url (r'^fk/', include ('fk.urls')), # фронт кик
url (r'^hk/', include ('hk.urls')), # хай кик
url (r'^ak/', include ('ak.urls')), # ап кик

url (r'^borba/', include ('borba.urls')), # борьба
url (r'^borba/', include ('backmount.urls')), # борьба и удущение
url (r'^borba/', include ('mount.urls')), # маунт соперник с верху
url (r'^borba/', include ('sidemount.urls')), # соперник с боку
url(r'^admin/', include(admin.site.urls)),
)
