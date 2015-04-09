# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0003_auto_20150408_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicaciones',
            name='historia',
            field=models.OneToOneField(to='historias.Historias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='sala',
            field=models.CharField(max_length=10, choices=[(b'SALA 1', b'SALA 1'), (b'SALA 2', b'SALA 1'), (b'SALA 3', b'SALA 3'), (b'SALA 4', b'SALA 4'), (b'SALA 5', b'SALA 5'), (b'GAURDIA', b'GAURDIA'), (b'NEO', b'NEO'), (b'UTI', b'UTI'), (b'UCO', b'UCO'), (b'PRE PARTO', b'PRE PARTO')]),
            preserve_default=True,
        ),
    ]
