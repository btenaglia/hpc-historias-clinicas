# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fojasquirurgicas',
            name='procedimiento_quirurgico',
            field=models.TextField(default=1, verbose_name='Procedimiento Quirurgico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 1, 17, 50, 54, 580553)),
            preserve_default=True,
        ),
    ]
