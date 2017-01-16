# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yumor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yumorcl',
            old_name='text',
            new_name='text_ckred',
        ),
    ]
