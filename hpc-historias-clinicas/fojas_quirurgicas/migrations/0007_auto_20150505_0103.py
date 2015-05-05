# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('procedimientos_quirurgicos', '0001_initial'),
        ('fojas_quirurgicas', '0006_auto_20150505_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='fojasquirurgicas',
            name='procedimiento_quirurgico',
            field=models.ForeignKey(default=1, to='procedimientos_quirurgicos.ProcedimientosQuirurgicos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 1, 3, 4, 302881)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_comienzo',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 3, 4, 302931), verbose_name='Hora / Comienzo Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_fin',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 1, 3, 4, 302965), verbose_name='Hora / Termin\xf3 Operac\xf3n'),
            preserve_default=True,
        ),
    ]
