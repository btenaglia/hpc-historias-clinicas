# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antecedentes_personales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='alergia',
            field=models.TextField(default='Niega', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='antecedentes_quirurgicos',
            field=models.TextField(default='Niega', null=True, verbose_name='Antecedentes Quir\xfargicos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='antecedentes_traumaticos',
            field=models.TextField(default='Niega', null=True, verbose_name='Antecedentes Traum\xe1ticos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='enfermedad_adulto',
            field=models.TextField(default='Niega', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='enfermedad_infantil',
            field=models.TextField(default='Niega', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antecedentespersonales',
            name='internaciones_previas',
            field=models.TextField(default='Niega', null=True, blank=True),
            preserve_default=True,
        ),
    ]
