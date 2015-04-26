# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0012_auto_20150425_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicaciones',
            name='comentario',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='dpto_cirugia',
            field=models.ForeignKey(verbose_name='Dpto. Cirug\xeda', to='historias.DptosCirugiaGeneral'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2015, 4, 26, 15, 41, 22, 228229), help_text='Formato: dd/mm/yyyy', verbose_name='Fecha de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historias',
            name='hora_ingreso',
            field=models.TimeField(default=datetime.datetime(2015, 4, 26, 15, 41, 22, 228181), help_text='Formato: hh:mm', verbose_name='Hora de Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='cama',
            field=models.CharField(max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'11bis', b'11bis'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31'), (b'32', b'32'), (b'Otros', b'Otros')]),
            preserve_default=True,
        ),
    ]
