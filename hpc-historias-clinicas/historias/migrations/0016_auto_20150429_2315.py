# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0015_auto_20150426_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 29, 23, 15, 17, 703856), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 29, 23, 15, 17, 703802), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='comentario',
            field=models.CharField(help_text='Campo \xfatil para indicar el n\xfamero o nombre de camas no proporcionadas por el sistema', max_length=20, null=True, verbose_name='Comentario para una cama', blank=True),
            preserve_default=True,
        ),
    ]
