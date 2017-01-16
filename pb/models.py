# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class PbClass (models.Model):
    class Meta ():
        db_table = 'pb_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    pb_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    pb_text = models.TextField (verbose_name='текст', blank=True, )
    pb_date = models.DateTimeField (verbose_name='Дата',)
    #onesite_text1 = models.TextField(verbose_name='текст1', blank=True, null=True, )

    def __unicode__(self):
        return self.pb_title