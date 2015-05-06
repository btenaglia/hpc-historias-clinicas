# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparatos', '0002_auto_20150413_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparatos',
            name='cardiovasculares',
            field=models.TextField(default=b'Niega hipertensi\xc3\xb3n, hipotensi\xc3\xb3n, precordialgias, palpitaciones, disnea de esfuerzo, disnea de reposo, disnea parox\xc3\xadstica noctura, ortopnea, claudicaci\xc3\xb3n intermitente, cianosis, edemas, varices. Foco para Chagas negativo', null=True, verbose_name='Ap. Cardiovasculares', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='digestivo',
            field=models.TextField(default=b'Niega disfagia, disglusia, odinofagia, pirosis, ardor epigastrico, nauseas, vomitos, hematemesis, melena enterorragia proctorragia, cambio en el habito evacuatorio, pujos y tenesmo rectal, ictericia coluria y acolia, hepatitis y parasitosis.', null=True, verbose_name='Ap. Digestivo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='genital',
            field=models.TextField(default=b'Menarca:  a\xc3\xb1os, FUM: hace   a\xc3\xb1os, Gestas: / Paras:  , niega anticoncepci\xc3\xb3n, flujo vaginal, metrorragias, nodulos mamarios secreci\xc3\xb3n por el pez\xc3\xb3n', null=True, verbose_name='Ap. Genital', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='locomotor',
            field=models.TextField(default='Sin particularidades', null=True, verbose_name='Ap. Locomotor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='organos',
            field=models.TextField(default='Sin particularidades', null=True, verbose_name='Organos de los Sentidos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='piel_faneas',
            field=models.TextField(default='Sin particularidades', null=True, verbose_name='Piel y Faneas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='respiratorio',
            field=models.TextField(default=b'Niega: tos, expectoraci\xc3\xb3n, dolor toraxico, asma, broncoespasmo,neumon\xc3\xada, hemoptisis, v\xc3\xb3mica, derrame pleural. Foco para tuberculosis negativo', null=True, verbose_name='Ap. Respiratorio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='sistema_endocrino',
            field=models.TextField(default=b'Niega: diabetes y otrasendocrinopat\xc3\xadas', null=True, verbose_name='Sistema Endocrino', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='sistema_nervioso',
            field=models.TextField(default=b'Niega: cefaleas, mareos, epilepsia, convulsiones, p\xc3\xa9rdida de conocimiento, y otros trastornos  sensoriales, sensitivos y motores.', null=True, verbose_name='Sistema Nervioso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='urinario',
            field=models.TextField(default=b'Niega: disuria, polaquiuria, poliurja, hematuria, piuria, litiasis urinaria, c\xc3\xb3lico renal, pujos y tenesmo vesical, infecciones urinarias o repetici\xc3\xb3n.', null=True, verbose_name='Ap. Urinario', blank=True),
            preserve_default=True,
        ),
    ]
