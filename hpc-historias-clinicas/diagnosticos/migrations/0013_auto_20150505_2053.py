# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0012_auto_20150505_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 287390), help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 287447), help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
