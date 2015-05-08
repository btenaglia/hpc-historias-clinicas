# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metodologias', '0003_auto_20150507_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodologias',
            name='historia',
            field=models.ForeignKey(blank=True, to='historias.Historias', null=True),
            preserve_default=True,
        ),
    ]
