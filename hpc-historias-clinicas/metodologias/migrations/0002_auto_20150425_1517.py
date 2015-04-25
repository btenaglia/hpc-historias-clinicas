# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metodologias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMetodologias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=150, verbose_name='Metodolog\xeda')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='metodologias',
            name='tipo_metodologia',
            field=models.ForeignKey(verbose_name='Metodolog\xeda', blank=True, to='metodologias.TipoMetodologias', null=True),
            preserve_default=True,
        ),
    ]
