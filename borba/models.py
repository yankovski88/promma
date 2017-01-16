# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class BorbaClass (models.Model):
    class Meta ():
        db_table = 'borba_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    borba_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    borba_text = models.TextField (verbose_name='текст', blank=True, )
    #borba_text = RichTextField(verbose_name='текст', blank=True, )
    borba_date = models.DateTimeField (verbose_name='Дата',)


    def __unicode__(self):
        return self.borba_title