# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen_fisico', '0003_auto_20150505_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenfisico',
            name='abdomen',
            field=models.TextField(default=b'Plano, sim\xc3\xa9trico, sin cicatrices ni signos de hepatopat\xc3\xadas cr\xc3\xb3nicas. Blando, depresible e indoloro. Borde superior del h\xc3\xadgado en 6\xc2\xba espacio intercostal.No palpo h\xc3\xadgado, bazo, ni otras organomegalias. Traube desocupado, timpanismo abdominal conservado. RHA + Pu\xc3\xb1o percusi\xc3\xb3n bilateral negativa.', null=True, verbose_name='Abdomen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='cabeza_cuello',
            field=models.TextField(default=b'Normoc\xc3\xa9falo, con buena implantaci\xc3\xb3n pilosa, escleras claras, conjuntivas rosadas, pupilas isoc\xc3\xb3ricas y reactivas, buena motilidad intr\xc3\xadnseca y extr\xc3\xadnseca, mucosas h\xc3\xbamedas, fosas nasales sin secreciones, orofaringe no congestiva, lengua roja, central y m\xc3\xb3vil, dentadura en mal estado, sin pr\xc3\xb3tesis dentaria. Cuello cil\xc3\xadndrico, sin cicatrices ingurgitaci\xc3\xb3n yugular 2/6 sin colapso inspiratorio, pulsos carot\xc3\xaddeos presentes, sin soplos. No palpo tiroides ni adenomegalias.', null=True, verbose_name='Cabeza y Cuello', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='cardiovascular',
            field=models.TextField(default=b'Latido apexiano en 5\xc2\xba espacio intercostal, l\xc3\xadnea hemiclavicular, ruidos netos, silencios libres. Pulso regular, sin signos de descompensaci\xc3\xb3n hemodin\xc3\xa1mica.', null=True, verbose_name='Ap. Cardiovascular', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='examen_proctologico',
            field=models.TextField(default=b'Sin patolog\xc3\xada orificial. Esfinter t\xc3\xb3nico, mucosa rectal lisa y deslizable. Douglas que no duele ni abomba, espacion perimetrales libres. Ampolla rectal desocupada.', null=True, verbose_name='Ex\xe1men Proctol\xf3gico', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='miembros',
            field=models.TextField(default=b'Sim\xc3\xa9tricos, sin cicatrices.Tono, trofismo, temperatura, sensibilidad y movilidad conservada. Pulsos perif\xc3\xa9ricos presentes, sin soplos. No palpo adenopat\xc3\xadas.', null=True, verbose_name='Miembros', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='examenfisico',
            name='torax',
            field=models.TextField(default=b'T\xc3\xb3rax sim\xc3\xa9trico, sin cicatrices no tiraje intercostal, sonoridad pulmonar y de columna vertebral conservada, buena expansi\xc3\xb3n de bases y v\xc3\xa9rtices, murmullo vesicular presente, buena entrada bilateral de aires sin ruidos agregados.', null=True, verbose_name='T\xf3rax', blank=True),
            preserve_default=True,
        ),
    ]
