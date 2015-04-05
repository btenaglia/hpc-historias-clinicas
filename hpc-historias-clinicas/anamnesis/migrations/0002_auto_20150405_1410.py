# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesis',
            name='motivo_consulta',
            field=models.ForeignKey(verbose_name='Motivo de consulta', to='anamnesis.MotivosConsultas'),
            preserve_default=True,
        ),
    ]
