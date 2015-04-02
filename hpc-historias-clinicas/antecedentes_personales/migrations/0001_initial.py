# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentesPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('enfermedad_infantil', models.TextField(default='Niega')),
                ('enfermedad_adulto', models.TextField(default='Niega')),
                ('alergia', models.TextField(default='Niega')),
                ('antecedentes_traumaticos', models.TextField(default='Niega', verbose_name='Antecedentes Traum\xe1ticos')),
                ('antecedentes_quirurgicos', models.TextField(default='Niega', verbose_name='Antecedentes Quir\xfargicos')),
                ('internaciones_previas', models.TextField(default='Niega')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
