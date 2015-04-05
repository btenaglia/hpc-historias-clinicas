# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticos',
            name='fecha',
            field=models.DateField(help_text='Formato: dd/mm/yyyy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diagnosticos',
            name='hora',
            field=models.TimeField(help_text='Formato: hh:mm'),
            preserve_default=True,
        ),
    ]
