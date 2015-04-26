# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20150426_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 26, 15, 45, 54, 670471), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 26, 15, 45, 54, 670421), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
