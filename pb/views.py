# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from pb.models import PbClass
# проверка или удалятся файлы закинутые вручную на сервере
def pb (request):
    pb1 = PbClass.objects.all()
    return render_to_response('pb.html', {'pb2': pb1})

# Create your views here.
