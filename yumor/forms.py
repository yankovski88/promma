# -*- coding: utf-8 -*-
from django.forms import ModelForm # импортировали нашу форму
from yumor.models import YumorCl # импортируем наш класс с моделей

class YumorForm (ModelForm): # ну и создаем наш класс с добовление Form  и вставляем нашу форму
    class Meta:
        model = YumorCl # cтандартная запись к модели
        fields = ['title', 'text_ckred'] # добавили наши поля с моделей