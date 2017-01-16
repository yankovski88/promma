# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lk.models import LkClass
# проверка или удалятся файлы закинутые вручную на сервере
def lk (request):
    lk1 = LkClass.objects.all()
    return render_to_response('lk.html', {'lk2': lk1})

# Create your views here.
