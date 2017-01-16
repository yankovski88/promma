# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lp.models import LpClass
# проверка или удалятся файлы закинутые вручную на сервере
def lp (request):
    lp1 = LpClass.objects.all()
    return render_to_response('lp.html', {'lppp': lp1})

# Create your views here.
