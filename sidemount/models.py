# -*- coding: utf-8 -*-
from django.db import models
#from ckeditor.fields import RichTextField # импорт ckeditor
# Create your models here.

class SidemountClass (models.Model):
    class Meta ():
        db_table = 'sidemount_class' # теперь мы будем знать к чему относиться наша модель или ее название
    '''
    наша стандартная модель
    '''
    sidemount_title = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    sidemount_text = models.TextField (verbose_name='текст', blank=True, )
    #bk_text = RichTextField(verbose_name='текст', blank=True, )
    sidemount_date = models.DateTimeField (verbose_name='Дата',)


    def __unicode__(self):
        return self.sidemount_title