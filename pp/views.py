# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from pp.models import PpClass
# проверка или удалятся файлы закинутые вручную на сервере
def pp (request):
    pp1 = PpClass.objects.all()
    return render_to_response('pp.html', {'pp1': pp1})

# Create your views here.
