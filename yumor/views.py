# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect # будет сообщать что форма отправлена успешно
from yumor.forms import YumorForm # импортировали наш класс с формс
from yumor.forms import YumorCl # имп


def yumor_name (request):
    if request.method == 'POST': # отправим данные методом POST
        form = YumorForm (request.POST) # создали форму для словаря


        if form.is_valid():
            print form.cleaned_data # все что правильно заполненое вывести
            form.save() # форму сохранить
        return HttpResponseRedirect ('/dobavit/redirect/') # пишем перевести на другую страницу все правильно

    else:
        form = YumorForm() # иначе вернуть обратно форму
    return render(request, 'yumorform.html', {'form': form}) #



def yumor_redirect (request):
    return render_to_response('redirect.html')



def yumor_base (request):
    yumor_base1 = YumorCl.objects.all()
    return render_to_response('yumor.html', {'yumor_base2': yumor_base1})