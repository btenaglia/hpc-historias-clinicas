# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('cardiovasculares', models.TextField(verbose_name='Ap. Cardiovasculares')),
                ('respiratorio', models.TextField(verbose_name='Ap. Respiratorio')),
                ('digestivo', models.TextField(verbose_name='Ap. Digestivo')),
                ('urinario', models.TextField(verbose_name='Ap. Urinario')),
                ('genital', models.TextField(verbose_name='Ap. Genital')),
                ('locomotor', models.TextField(verbose_name='Ap. Locomotor')),
                ('sistema_nervioso', models.TextField(verbose_name='Sistema Nervioso')),
                ('sistema_endocrino', models.TextField(verbose_name='Sistema Endocrino')),
                ('piel_faneas', models.TextField(verbose_name='Piel y Faneas')),
                ('organos', models.TextField(verbose_name='Organos de los Sentidos')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
