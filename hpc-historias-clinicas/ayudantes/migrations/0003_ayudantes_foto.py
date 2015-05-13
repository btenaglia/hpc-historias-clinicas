# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ayudantes', '0002_auto_20150327_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayudantes',
            name='foto',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'ayudantes_fotos', null=True, verbose_name='Foto del ayudante', blank=True),
            preserve_default=True,
        ),
    ]
