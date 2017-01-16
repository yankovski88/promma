# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from hk.models import HkClass
# проверка или удалятся файлы закинутые вручную на сервере
def hk (request):
    hk1 = HkClass.objects.all()
    return render_to_response('hk.html', {'hk2': hk1})

# Create your views here.
