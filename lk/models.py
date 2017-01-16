# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class LkClass (models.Model):
    class Meta ():
        db_table = 'lk_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    lk_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    lk_text = models.TextField (verbose_name='текст', blank=True, )
    #pp_text = RichTextField(verbose_name='текст', blank=True, )
    lk_date = models.DateTimeField (verbose_name='Дата',)


    def __unicode__(self):
        return self.lk_title