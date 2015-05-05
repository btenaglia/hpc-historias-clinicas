# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('evoluciones', '0005_auto_20150426_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evoluciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 0, 54, 34, 523194)),
            preserve_default=True,
        ),
    ]
