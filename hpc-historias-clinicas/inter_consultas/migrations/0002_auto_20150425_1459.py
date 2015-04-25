# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inter_consultas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interconsultas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 14, 59, 14, 471493)),
            preserve_default=True,
        ),
    ]
