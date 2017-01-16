# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from po.models import PoClass
# проверка или удалятся файлы закинутые вручную на сервере
def po (request):
    po1 = PoClass.objects.all()
    return render_to_response('po.html', {'po2': po1})

# Create your views here.
