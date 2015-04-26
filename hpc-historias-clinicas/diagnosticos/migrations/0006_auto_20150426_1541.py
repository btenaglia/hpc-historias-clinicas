# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0005_auto_20150425_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 4, 26, 15, 41, 22, 217722), help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 4, 26, 15, 41, 22, 217776), help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
