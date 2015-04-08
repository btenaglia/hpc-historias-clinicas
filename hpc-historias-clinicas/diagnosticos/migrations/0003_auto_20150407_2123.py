# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0002_auto_20150405_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='tipo_diagnostico',
            field=models.ForeignKey(verbose_name='Diagn\xf3stico', blank=True, to='diagnosticos.TipoDiagnosticos', null=True),
            preserve_default=True,
        ),
    ]
