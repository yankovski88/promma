# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from ak.models import AkClass
# проверка или удалятся файлы закинутые вручную на сервере
def ak (request):
    ak1 = AkClass.objects.all()
    return render_to_response('ak.html', {'ak2': ak1})

# Create your views here.
