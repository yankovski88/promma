# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from fk.models import FkClass
# проверка или удалятся файлы закинутые вручную на сервере
def fk (request):
    fk1 = FkClass.objects.all()
    return render_to_response('fk.html', {'fk2': fk1})

# Create your views here.
