# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import braces.views._access


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayudantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField(max_length=8)),
            ],
            options={
                'abstract': False,
            },
            bases=(braces.views._access.LoginRequiredMixin, models.Model),
        ),
    ]
