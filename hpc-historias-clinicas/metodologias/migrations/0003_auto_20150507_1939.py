# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0024_auto_20150507_1939'),
        ('metodologias', '0002_auto_20150425_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metodologias',
            name='metodologia',
        ),
        migrations.AddField(
            model_name='metodologias',
            name='historia',
            field=models.ForeignKey(blank=True, to='historias.Historias', null=True),
            preserve_default=False,
        ),
    ]
