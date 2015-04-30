# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ayudantes', '0002_auto_20150327_0026'),
        ('medicos', '0002_auto_20150327_0024'),
        ('historias', '0016_auto_20150429_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='FojasQuirurgicas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateField(default=datetime.datetime(2015, 4, 29, 23, 15, 17, 710925))),
                ('hora_comienzo', models.TimeField(verbose_name='Hora / Comienzo Operac\xf3n')),
                ('hora_fin', models.TimeField(verbose_name='Hora / Termin\xf3 Operac\xf3n')),
                ('ayudante_1', models.ForeignKey(related_name='ayudante_1', verbose_name='1er Ayudante', to='ayudantes.Ayudantes')),
                ('ayudante_2', models.ForeignKey(related_name='ayudante_2', verbose_name='2er Ayudante', to='ayudantes.Ayudantes')),
                ('ayudante_3', models.ForeignKey(related_name='ayudante_3', verbose_name='3er Ayudante', to='ayudantes.Ayudantes')),
                ('cirujano', models.ForeignKey(to='medicos.Medicos')),
                ('historia', models.ForeignKey(to='historias.Historias')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
