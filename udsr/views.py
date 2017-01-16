# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from udsr.models import UdsrClass
# проверка или удалятся файлы закинутые вручную на сервере
def udsr (request):
    udsr1 = UdsrClass.objects.all()
    return render_to_response('udsr.html', {'udsr2': udsr1})

# Create your views here.
