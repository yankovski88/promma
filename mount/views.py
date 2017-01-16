# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from mount.models import MountClass
# проверка или удалятся файлы закинутые вручную на сервере
def mount (request):
    mount1 = MountClass.objects.all()
    return render_to_response('mount.html', {'mount2': mount1})

# Create your views here.
