# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0007_auto_20150505_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 411938)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_comienzo',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 411995), verbose_name='Hora / Comienzo Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='hora_fin',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 412034), verbose_name='Hora / Termin\xf3 Operac\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='procedimiento_quirurgico',
            field=models.ForeignKey(verbose_name=b'Nombre del procedimiento quir\xc3\xbargico', to='procedimientos_quirurgicos.ProcedimientosQuirurgicos'),
            preserve_default=True,
        ),
    ]
