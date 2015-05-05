# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0005_auto_20150505_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fojasquirurgicas',
            old_name='procedimiento_quirurgico',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 1, 2, 7, 654751)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_comienzo',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 2, 7, 654803), verbose_name='Hora / Comienzo Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_fin',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 2, 7, 654838), verbose_name='Hora / Termin\xf3 Operac\xf3n'),
            preserve_default=True,
        ),
    ]
