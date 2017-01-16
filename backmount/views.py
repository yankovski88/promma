# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from backmount.models import BackmountClass
# проверка или удалятся файлы закинутые вручную на сервере
def backmount (request):
    backmount1 = BackmountClass.objects.all()
    return render_to_response('backmount.html', {'backmount2': backmount1})

# Create your views here.
