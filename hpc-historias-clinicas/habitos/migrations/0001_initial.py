# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('alcohol', models.CharField(max_length=150, null=True, blank=True)),
                ('tabaco', models.CharField(max_length=150, null=True, blank=True)),
                ('cafe', models.CharField(max_length=150, null=True, verbose_name='Caf\xe9', blank=True)),
                ('dieta', models.CharField(max_length=150, null=True, blank=True)),
                ('drogadiccion', models.CharField(max_length=150, null=True, verbose_name='Drogadicci\xf3n', blank=True)),
                ('sueno', models.CharField(max_length=150, null=True, verbose_name='Sue\xf1o', blank=True)),
                ('medicamentos', models.TextField(null=True, blank=True)),
                ('catarsis', models.CharField(max_length=150, null=True, blank=True)),
                ('diuresis', models.CharField(max_length=150, null=True, blank=True)),
                ('peso', models.FloatField(max_length=150, null=True, blank=True)),
                ('talla', models.FloatField(max_length=150, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
