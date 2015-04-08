# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_auto_20150405_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('sala', models.CharField(max_length=10, choices=[(b'SALA 1', b'SALA 1'), (b'SALA 2', b'SALA 1')])),
                ('cama', models.CharField(max_length=10, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('historia', models.ForeignKey(to='historias.Historias')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='ubicaciones',
            unique_together=set([('sala', 'cama')]),
        ),
        migrations.AlterField(
            model_name='historias',
            name='paciente',
            field=models.ForeignKey(to='pacientes.Pacientes'),
            preserve_default=True,
        ),
    ]
