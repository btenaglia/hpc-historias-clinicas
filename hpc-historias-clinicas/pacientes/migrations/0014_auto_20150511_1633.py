# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0013_auto_20150506_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='foto',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'pacientes_fotos', null=True, verbose_name='Foto del paciente', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 5, 11, 16, 33, 14, 32502), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 5, 11, 16, 33, 14, 32449), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
    ]
