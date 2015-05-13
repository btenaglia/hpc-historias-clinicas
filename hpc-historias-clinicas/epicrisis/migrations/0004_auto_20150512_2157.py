# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epicrisis', '0003_auto_20150510_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epicrisis',
            name='fecha_proxima_consulta',
            field=models.DateField(null=True, verbose_name='Fecha de la pr\xf3xima consulta', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='epicrisis',
            name='hora_proxima_consulta',
            field=models.TimeField(null=True, verbose_name='Hora de la pr\xf3xima consulta', blank=True),
            preserve_default=True,
        ),
    ]
