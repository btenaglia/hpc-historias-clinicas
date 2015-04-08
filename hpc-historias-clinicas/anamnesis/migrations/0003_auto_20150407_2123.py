# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0002_auto_20150405_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesis',
            name='motivo_consulta',
            field=models.ForeignKey(verbose_name='Motivo de consulta', blank=True, to='anamnesis.MotivosConsultas', null=True),
            preserve_default=True,
        ),
    ]
