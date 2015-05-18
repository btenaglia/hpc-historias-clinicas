# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('evoluciones', '0011_auto_20150506_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evoluciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 18, 0, 59, 24, 74873)),
            preserve_default=True,
        ),
    ]
