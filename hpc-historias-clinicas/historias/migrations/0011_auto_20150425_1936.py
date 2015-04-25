# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0010_auto_20150425_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='historias',
            name='dpto_cirugia',
            field=models.ForeignKey(verbose_name='M\xe9dico Responsable', blank=True, to='historias.DptosCirugiaGeneral', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 19, 36, 57, 301013), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 25, 19, 36, 57, 300963), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
