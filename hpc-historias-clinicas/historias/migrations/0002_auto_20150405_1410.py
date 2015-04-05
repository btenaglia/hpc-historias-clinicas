# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 5, 14, 9, 50, 704437), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 5, 14, 10, 7, 758430), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=False,
        ),
    ]
