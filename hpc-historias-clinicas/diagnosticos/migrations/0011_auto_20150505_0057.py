# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0010_auto_20150505_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 0, 56, 59, 519410), help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 5, 5, 0, 56, 59, 519458), help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
