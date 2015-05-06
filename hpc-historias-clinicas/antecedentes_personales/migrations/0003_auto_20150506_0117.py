# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antecedentes_personales', '0002_auto_20150413_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='antecedentes_quirurgicos',
            field=models.TextField(default='Niega cirug\xedas previas', null=True, verbose_name='Antecedentes Quir\xfargicos', blank=True),
            preserve_default=True,
        ),
    ]
