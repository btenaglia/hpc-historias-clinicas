# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0004_auto_20150504_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 1, 1, 1, 702694)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_comienzo',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 1, 1, 702739), verbose_name='Hora / Comienzo Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_fin',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 1, 1, 702778), verbose_name='Hora / Termin\xf3 Operac\xf3n'),
            preserve_default=True,
        ),
    ]
