# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from sidemount.models import SidemountClass
# проверка или удалятся файлы закинутые вручную на сервере
def sidemount (request):
    sidemount1 = SidemountClass.objects.all()
    return render_to_response('sidemount.html', {'sidemount2': sidemount1})

# Create your views here.
