# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from bk.models import BkClass
# проверка или удалятся файлы закинутые вручную на сервере
def bk (request):
    bk1 = BkClass.objects.all()
    return render_to_response('bk.html', {'bk2': bk1})

# Create your views here.
