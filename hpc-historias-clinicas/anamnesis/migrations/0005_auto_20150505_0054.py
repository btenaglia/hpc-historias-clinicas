# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0004_motivosconsultas_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesis',
            name='enfermedad_actual',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='motivosconsultas',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n', blank=True),
            preserve_default=True,
        ),
    ]
