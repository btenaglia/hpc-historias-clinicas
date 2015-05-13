# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_auto_20150327_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicos',
            name='foto',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'medicos_fotos', null=True, verbose_name='Foto del m\xe9dico', blank=True),
            preserve_default=True,
        ),
    ]
