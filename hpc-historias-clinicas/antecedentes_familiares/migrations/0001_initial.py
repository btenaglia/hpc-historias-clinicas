# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentesFamiliares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('padre', models.CharField(max_length=150, null=True, blank=True)),
                ('madre', models.CharField(max_length=150, null=True, blank=True)),
                ('hermanos', models.CharField(max_length=150, null=True, blank=True)),
                ('hijos', models.CharField(max_length=150, null=True, blank=True)),
                ('otros', models.TextField(max_length=150, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
