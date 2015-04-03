# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen_fisico', '0001_initial'),
        ('antecedentes_personales', '0001_initial'),
        ('pacientes', '0003_auto_20150327_0026'),
        ('antecedentes_familiares', '0001_initial'),
        ('aparatos', '0001_initial'),
        ('planteos', '0001_initial'),
        ('metodologias', '0001_initial'),
        ('diagnosticos', '0001_initial'),
        ('anamnesis', '0001_initial'),
        ('habitos', '0002_habitos_sexualidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.CharField(max_length=10)),
                ('tipo', models.IntegerField(default=1, choices=[(1, b'Internaci\xc3\xb3n'), (2, b'Inter Consulta')])),
                ('estado', models.IntegerField(blank=True, null=True, choices=[(1, b'Alta'), (2, b'\xc3\x93bito'), (3, b'Pase de servicio')])),
                ('anamnesis', models.OneToOneField(to='anamnesis.Anamnesis')),
                ('antecedentes_familiares', models.OneToOneField(to='antecedentes_familiares.AntecedentesFamiliares')),
                ('antecedentes_personales', models.OneToOneField(to='antecedentes_personales.AntecedentesPersonales')),
                ('aparatos', models.OneToOneField(to='aparatos.Aparatos')),
                ('diagnostico', models.OneToOneField(to='diagnosticos.Diagnosticos')),
                ('examen_fisico', models.OneToOneField(to='examen_fisico.ExamenFisico')),
                ('habitos', models.OneToOneField(to='habitos.Habitos')),
                ('metodologias', models.OneToOneField(to='metodologias.Metodologias')),
                ('paciente', models.OneToOneField(to='pacientes.Pacientes')),
                ('planteos', models.OneToOneField(to='planteos.Planteos')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
