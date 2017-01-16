# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lb.models import LbClass
# проверка или удалятся файлы закинутые вручную на сервере
def lb (request):
    lp1 = LbClass.objects.all()
    return render_to_response('lb.html', {'lb2': lp1})

# Create your views here.
