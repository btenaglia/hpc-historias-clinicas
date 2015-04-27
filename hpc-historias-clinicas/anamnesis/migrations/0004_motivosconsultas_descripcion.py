# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0003_auto_20150407_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='motivosconsultas',
            name='descripcion',
            field=models.TextField(help_text='Descripci\xf3n', null=True, blank=True),
            preserve_default=True,
        ),
    ]
