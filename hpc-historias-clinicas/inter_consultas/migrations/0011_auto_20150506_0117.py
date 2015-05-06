# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inter_consultas', '0010_auto_20150505_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interconsultas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 1, 17, 17, 367240)),
            preserve_default=True,
        ),
    ]
