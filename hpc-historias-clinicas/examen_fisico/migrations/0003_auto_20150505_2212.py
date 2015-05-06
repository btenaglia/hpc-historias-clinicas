# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen_fisico', '0002_auto_20150413_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='examenfisico',
            name='cabeza_cuello',
            field=models.TextField(null=True, verbose_name='Cabeza y Cuello', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='impresion_general',
            field=models.TextField(default=b'Paciente l\xc3\xbacido/a, orientada en tiempo y espacio dec\xc3\xbabito activo e indiferente, que impresiona enferma.', null=True, verbose_name='Impresi\xf3n General', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='signos_vitales',
            field=models.TextField(null=True, verbose_name='Signos Vitales P.A.F.C.F.R Peso', blank=True),
            preserve_default=True,
        ),
    ]
