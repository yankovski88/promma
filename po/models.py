# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class PoClass (models.Model):
    class Meta ():
        db_table = 'po_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    po_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    po_text = models.TextField (verbose_name='текст', blank=True, )
    #po_text = models.TextField(verbose_name='текст1', blank=True, null=True, )
    po_date = models.DateTimeField (verbose_name='Дата',)


    def __unicode__(self):
        return self.po_title