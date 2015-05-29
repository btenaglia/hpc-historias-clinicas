# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('evoluciones', '0012_auto_20150518_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('foto', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'evoluciones_fotos')),
                ('comentario', models.TextField(null=True, blank=True)),
                ('evolucion', models.ForeignKey(to='evoluciones.Evoluciones')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='evoluciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 16, 58, 30, 725212)),
            preserve_default=True,
        ),
    ]
