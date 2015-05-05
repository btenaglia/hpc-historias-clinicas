# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fojas_quirurgicas', '0002_auto_20150501_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='ayudante_1',
            field=models.ForeignKey(related_name='ayudante_1', verbose_name='1er Ayudante', blank=True, to='ayudantes.Ayudantes', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='ayudante_2',
            field=models.ForeignKey(related_name='ayudante_2', verbose_name='2er Ayudante', blank=True, to='ayudantes.Ayudantes', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='ayudante_3',
            field=models.ForeignKey(related_name='ayudante_3', verbose_name='3er Ayudante', blank=True, to='ayudantes.Ayudantes', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fojasquirurgicas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 4, 21, 16, 56, 980535)),
            preserve_default=True,
        ),
    ]
