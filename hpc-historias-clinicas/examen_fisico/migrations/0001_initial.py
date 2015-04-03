# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('impresion_general', models.TextField(verbose_name='Impresi\xf3n General')),
                ('signos_vitales', models.TextField(verbose_name='Signos Vitales P.A.F.C.F.R Peso Cabez y Cuello')),
                ('torax', models.TextField(verbose_name='Torax')),
                ('respiratorio', models.TextField(verbose_name='Ap. Respiratorio')),
                ('cardiovascular', models.TextField(verbose_name='Ap. Cardiovascular')),
                ('abdomen', models.TextField(verbose_name='Abdomen')),
                ('miembros', models.TextField(verbose_name='Miembros')),
                ('genitales', models.TextField(verbose_name='Genitales')),
                ('examen_neurologico', models.TextField(verbose_name='Ex\xe1men Neurol\xf3gico')),
                ('fondo_ojos', models.TextField(verbose_name='Fondo de Ojos')),
                ('examen_proctologico', models.TextField(verbose_name='Ex\xe1men Proctol\xf3gico')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
