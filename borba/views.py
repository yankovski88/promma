# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from borba.models import BorbaClass
# проверка или удалятся файлы закинутые вручную на сервере
def borba (request):
    borba1 = BorbaClass.objects.all()
    return render_to_response('borba.html', {'borba2': borba1})

# Create your views here.
