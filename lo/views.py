# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lo.models import LoClass
# проверка или удалятся файлы закинутые вручную на сервере
def lo (request):
    lo1 = LoClass.objects.all()
    return render_to_response('lo.html', {'lo2': lo1})

# Create your views here.
