# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from uroki.models import UrokiClass

def uroki (request):
    uroki1 = UrokiClass.objects.all()
    return render_to_response('uroki.html', {'uroki1': uroki1})

# Create your views here.
