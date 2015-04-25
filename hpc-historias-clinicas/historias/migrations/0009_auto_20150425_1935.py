# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_auto_20150327_0024'),
        ('historias', '0008_auto_20150425_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='DptosCirugiaGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='historias',
            name='medico',
            field=models.ForeignKey(verbose_name='M\xe9dico Responsable', blank=True, to='medicos.Medicos', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 25, 19, 35, 57, 784532), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 25, 19, 35, 57, 784483), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='sala',
            field=models.CharField(max_length=10, choices=[(b'SALA 1', b'SALA 1'), (b'SALA 2', b'SALA 2'), (b'SALA 3', b'SALA 3'), (b'SALA 4', b'SALA 4'), (b'SALA 5', b'SALA 5'), (b'GAURDIA', b'GAURDIA'), (b'NEO', b'NEO'), (b'UTI', b'UTI'), (b'UCO', b'UCO'), (b'PRE PARTO', b'PRE PARTO'), (b'CLARITA', b'CLARITA'), (b'HOSPITAL DE DIA', b'HOSPITAL DE DIA')]),
            preserve_default=True,
        ),
    ]
