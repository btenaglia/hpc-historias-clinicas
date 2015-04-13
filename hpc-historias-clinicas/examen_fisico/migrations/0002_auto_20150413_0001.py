# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen_fisico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenfisico',
            name='abdomen',
            field=models.TextField(null=True, verbose_name='Abdomen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='cardiovascular',
            field=models.TextField(null=True, verbose_name='Ap. Cardiovascular', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='examen_neurologico',
            field=models.TextField(null=True, verbose_name='Ex\xe1men Neurol\xf3gico', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='examen_proctologico',
            field=models.TextField(null=True, verbose_name='Ex\xe1men Proctol\xf3gico', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='fondo_ojos',
            field=models.TextField(null=True, verbose_name='Fondo de Ojos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='genitales',
            field=models.TextField(null=True, verbose_name='Genitales', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='impresion_general',
            field=models.TextField(null=True, verbose_name='Impresi\xf3n General', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='miembros',
            field=models.TextField(null=True, verbose_name='Miembros', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='respiratorio',
            field=models.TextField(null=True, verbose_name='Ap. Respiratorio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='signos_vitales',
            field=models.TextField(null=True, verbose_name='Signos Vitales P.A.F.C.F.R Peso Cabeza y Cuello', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='torax',
            field=models.TextField(null=True, verbose_name='Torax', blank=True),
            preserve_default=True,
        ),
    ]
