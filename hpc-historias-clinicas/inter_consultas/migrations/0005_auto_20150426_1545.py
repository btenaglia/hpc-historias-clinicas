# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inter_consultas', '0004_auto_20150426_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interconsultas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 26, 15, 45, 54, 691792)),
            preserve_default=True,
        ),
    ]
