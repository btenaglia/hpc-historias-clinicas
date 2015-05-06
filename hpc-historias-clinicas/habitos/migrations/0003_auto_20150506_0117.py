# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitos', '0002_habitos_sexualidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitos',
            name='alcohol',
            field=models.CharField(default='Ocacional', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='cafe',
            field=models.CharField(default='Ocacional', max_length=150, null=True, verbose_name='Caf\xe9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='catarsis',
            field=models.CharField(default='Conservada', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='dieta',
            field=models.CharField(default='Variada', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='diuresis',
            field=models.CharField(default='Conservada', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='drogadiccion',
            field=models.CharField(default='Niega', max_length=150, null=True, verbose_name='Drogadicci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='medicamentos',
            field=models.TextField(default='Niega', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='sexualidad',
            field=models.CharField(default='Heterosexual', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='sueno',
            field=models.CharField(default='Conservado', max_length=150, null=True, verbose_name='Sue\xf1o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='habitos',
            name='tabaco',
            field=models.CharField(default='Niega', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
