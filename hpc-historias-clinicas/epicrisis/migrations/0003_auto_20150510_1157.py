# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epicrisis', '0002_auto_20150510_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epicrisis',
            name='historia',
            field=models.ForeignKey(to='historias.Historias', unique=True),
            preserve_default=True,
        ),
    ]
