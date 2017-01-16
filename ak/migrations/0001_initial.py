# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AkClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ak_title', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba', blank=True)),
                ('ak_text', models.TextField(verbose_name=b'\xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('ak_date', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'db_table': 'ak_class',
            },
            bases=(models.Model,),
        ),
    ]
