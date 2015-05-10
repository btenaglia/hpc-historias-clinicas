# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epicrisis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epicrisis',
            name='tratamiento_alta',
            field=models.TextField(default='Control por consultorio externo. Curaciones de la herida. Antibi\xf3tico terapia.', null=True, verbose_name='Tratamiento al alta', blank=True),
            preserve_default=True,
        ),
    ]
