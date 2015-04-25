# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0006_auto_20150413_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 14, 59, 14, 468359), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 25, 14, 59, 14, 468307), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='sala',
            field=models.CharField(max_length=10, choices=[(b'SALA 1', b'SALA 1'), (b'SALA 2', b'SALA 2'), (b'SALA 3', b'SALA 3'), (b'SALA 4', b'SALA 4'), (b'SALA 5', b'SALA 5'), (b'GAURDIA', b'GAURDIA'), (b'NEO', b'NEO'), (b'UTI', b'UTI'), (b'UCO', b'UCO'), (b'PRE PARTO', b'PRE PARTO')]),
            preserve_default=True,
        ),
    ]
