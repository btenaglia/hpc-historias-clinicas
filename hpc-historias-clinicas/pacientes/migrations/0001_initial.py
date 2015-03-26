# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('sexo', models.IntegerField(max_length=1, choices=[(0, b'Masculino'), (1, b'Femenino')])),
                ('madre', models.CharField(max_length=300, verbose_name='Nombre y Apellido de la madre')),
                ('domicilio', models.CharField(max_length=100)),
                ('domicilio_numero', models.CharField(max_length=20, verbose_name='N\xfamero de domicilio')),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('edad', models.IntegerField(max_length=3)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('documento', models.IntegerField(max_length=8)),
                ('estado_civil', models.IntegerField(choices=[(0, b'Soltero'), (1, b'Casado'), (2, b'Viudo'), (3, b'Divorciado')])),
                ('ocupacion', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('procedencia', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('obra_social', models.CharField(max_length=100)),
                ('numero_afiliado', models.CharField(max_length=100)),
                ('hora_ingreso', models.TimeField(verbose_name='Hora de Ingreso')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de Ingreso')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
