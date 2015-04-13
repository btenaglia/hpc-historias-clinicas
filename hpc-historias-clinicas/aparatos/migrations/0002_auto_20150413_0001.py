# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparatos',
            name='cardiovasculares',
            field=models.TextField(null=True, verbose_name='Ap. Cardiovasculares', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='digestivo',
            field=models.TextField(null=True, verbose_name='Ap. Digestivo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='genital',
            field=models.TextField(null=True, verbose_name='Ap. Genital', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='locomotor',
            field=models.TextField(null=True, verbose_name='Ap. Locomotor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='organos',
            field=models.TextField(null=True, verbose_name='Organos de los Sentidos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='piel_faneas',
            field=models.TextField(null=True, verbose_name='Piel y Faneas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='respiratorio',
            field=models.TextField(null=True, verbose_name='Ap. Respiratorio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='sistema_endocrino',
            field=models.TextField(null=True, verbose_name='Sistema Endocrino', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='sistema_nervioso',
            field=models.TextField(null=True, verbose_name='Sistema Nervioso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='urinario',
            field=models.TextField(null=True, verbose_name='Ap. Urinario', blank=True),
            preserve_default=True,
        ),
    ]
