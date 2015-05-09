# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0025_auto_20150508_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epicrisis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('equipo_referencia', models.CharField(default='Cirug\xeda general', max_length=150, null=True, verbose_name='Equipo de referencia en la internaci\xf3n', blank=True)),
                ('antecedentes', models.TextField(null=True, verbose_name='Antecedentes', blank=True)),
                ('problemas', models.TextField(null=True, verbose_name='Detalle de los problemas abordados en el proceso actual', blank=True)),
                ('fecha_egreso', models.DateField(verbose_name='Fecha de egreso')),
                ('diagnostico_egreso', models.TextField(null=True, verbose_name='Diagn\xf3stico de egreso', blank=True)),
                ('resultado_examenes', models.TextField(null=True, verbose_name='Resultado de ex\xe1menes complementarios', blank=True)),
                ('laboratorio_alta', models.TextField(null=True, verbose_name='Laboratorio al alta', blank=True)),
                ('tratamiento_alta', models.TextField(default='Control por consultorio externo.Curaciones de la herida.Antibi\xf3tico terapia.', null=True, verbose_name='Tratamiento al alta', blank=True)),
                ('pendientes', models.TextField(null=True, verbose_name='Pendientes de resoluci\xf3n en el proceso de atenci\xf3n ambulatorio', blank=True)),
                ('equipo_referencia_alta', models.CharField(default='Cirug\xeda general, Otro', max_length=150, null=True, verbose_name='Equipo y centro de referencia al alta', blank=True)),
                ('fecha_proxima_consulta', models.DateField(verbose_name='Fecha de la pr\xf3xima consulta')),
                ('hora_proxima_consulta', models.TimeField(verbose_name='Hora de la pr\xf3xima consulta')),
                ('historia', models.ForeignKey(to='historias.Historias')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
