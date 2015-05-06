# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0021_auto_20150505_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 348659), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 348603), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
