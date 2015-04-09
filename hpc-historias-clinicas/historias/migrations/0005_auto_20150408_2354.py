# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0004_auto_20150408_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicaciones',
            name='historia',
            field=models.ForeignKey(to='historias.Historias', unique=True),
            preserve_default=True,
        ),
    ]
