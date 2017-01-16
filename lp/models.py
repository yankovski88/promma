# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class LpClass (models.Model):
    class Meta ():
        db_table = 'lp5_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    lp_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    lp_text = models.TextField (verbose_name='текст', blank=True, )
    # pp_text = RichTextField(verbose_name='текст', blank=True, )
    # verbose_name='текст' текст будет написан слева от нашей вставки сообщения (дополнительно),
    #blank = True  бланк может быть пустым, и текст (имя) будет не жирным
    # null = True и там ничего может не быть
    lp_date = models.DateTimeField (verbose_name='Дата',)
    #onesite_text1 = models.TextField(verbose_name='текст1', blank=True, null=True, )

    def __unicode__(self):
        return self.lp_title