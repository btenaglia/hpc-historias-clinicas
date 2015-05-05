# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inter_consultas', '0006_auto_20150505_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interconsultas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 0, 55, 44, 915470)),
            preserve_default=True,
        ),
    ]
