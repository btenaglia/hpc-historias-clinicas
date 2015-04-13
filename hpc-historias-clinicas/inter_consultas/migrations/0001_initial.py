# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0006_auto_20150413_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterConsultas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('historia', models.ForeignKey(to='historias.Historias')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
