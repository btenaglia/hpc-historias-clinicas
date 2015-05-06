# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antecedentes_familiares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='hermanos',
            field=models.CharField(default='Niega', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='hijos',
            field=models.CharField(default='Niega', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='madre',
            field=models.CharField(default='Viva, Sana', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='otros',
            field=models.TextField(default='Niega enfermedadase heredogen\xe9ticas', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='padre',
            field=models.CharField(default='Vivo, Sano', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
