# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('evoluciones', '0002_auto_20150425_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evoluciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 15, 27, 51, 779200)),
            preserve_default=True,
        ),
    ]
