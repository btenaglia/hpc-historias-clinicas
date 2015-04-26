# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inter_consultas', '0003_auto_20150425_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interconsultas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 26, 15, 41, 22, 231335)),
            preserve_default=True,
        ),
    ]
