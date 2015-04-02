# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosticos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(help_text='Escriba una descripcion si lo considera \xfatil', null=True, blank=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDiagnosticos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=150, verbose_name='Diagn\xf3stico')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diagnosticos',
            name='tipo_diagnostico',
            field=models.ForeignKey(verbose_name='Diagn\xf3stico', to='diagnosticos.TipoDiagnosticos'),
            preserve_default=True,
        ),
    ]
