# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0022_auto_20150506_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historias',
            name='metodologias',
        ),
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 5, 7, 19, 39, 19, 157927), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 5, 7, 19, 39, 19, 157874), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
