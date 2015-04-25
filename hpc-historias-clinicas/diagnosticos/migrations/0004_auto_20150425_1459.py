# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0003_auto_20150407_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 14, 59, 14, 459617), help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 4, 25, 14, 59, 14, 459671), help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
