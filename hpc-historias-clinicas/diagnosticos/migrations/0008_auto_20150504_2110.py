# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0007_auto_20150426_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosticos',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 4, 21, 10, 30, 438870), help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 5, 4, 21, 10, 30, 438925), help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
