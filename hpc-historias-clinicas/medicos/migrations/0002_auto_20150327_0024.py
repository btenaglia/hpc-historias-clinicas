# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='dni',
            field=models.IntegerField(unique=True, max_length=8),
            preserve_default=True,
        ),
    ]
