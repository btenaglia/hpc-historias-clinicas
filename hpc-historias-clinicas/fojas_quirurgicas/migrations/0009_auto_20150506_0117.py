# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0008_auto_20150505_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 402560)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_comienzo',
            field=models.TimeField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 402614), verbose_name='Hora / Comienzo Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_fin',
            field=models.TimeField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 402648), verbose_name='Hora / Termin\xf3 Operac\xf3n'),
            preserve_default=True,
        ),
    ]
