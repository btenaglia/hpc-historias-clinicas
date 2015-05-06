# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0020_auto_20150505_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 300641), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 20, 53, 29, 300571), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
