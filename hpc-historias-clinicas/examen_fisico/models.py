# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel

DEFAULT_IMPRESION_GENERAL = 'Paciente lúcido/a, orientada en tiempo y espacio ' \
                            'decúbito activo e indiferente, que impresiona enferma.'

DEFAULT_CABEZA_CUELLO = 'Normocéfalo, con buena implantación pilosa, escleras claras, ' \
                        'conjuntivas rosadas, pupilas isocóricas y reactivas, buena motilidad ' \
                        'intrínseca y extrínseca, mucosas húmedas, fosas nasales sin secreciones,' \
                        ' orofaringe no congestiva, lengua roja, central y móvil, dentadura en mal' \
                        ' estado, sin prótesis dentaria. Cuello cilíndrico, sin cicatrices ingurgitación' \
                        ' yugular 2/6 sin colapso inspiratorio, pulsos carotídeos presentes, sin soplos.' \
                        ' No palpo tiroides ni adenomegalias.'

DEFAULT_TORAX = 'Tórax simétrico, sin cicatrices no tiraje intercostal, sonoridad pulmonar y de ' \
                'columna vertebral conservada, buena expansión de bases y vértices, murmullo vesicular ' \
                'presente, buena entrada bilateral de aires sin ruidos agregados.'

DEFAULT_CARDIOVASCULAR = 'Latido apexiano en 5º espacio intercostal, línea hemiclavicular, ' \
                         'ruidos netos, silencios libres. Pulso regular, sin signos de ' \
                         'descompensación hemodinámica.'

DEFAULT_ABDOMEN = 'Plano, simétrico, sin cicatrices ni signos de hepatopatías crónicas. ' \
                  'Blando, depresible e indoloro. Borde superior del hígado en 6º espacio intercostal.' \
                  'No palpo hígado, bazo, ni otras organomegalias. Traube desocupado, timpanismo ' \
                  'abdominal conservado. RHA + Puño percusión bilateral negativa.'

DEFAULT_EXAMEN_PROCTOCOLOGICO = 'Sin patología orificial. Esfinter tónico, mucosa rectal lisa ' \
                                'y deslizable. Douglas que no duele ni abomba, espacion perimetrales ' \
                                'libres. Ampolla rectal desocupada.'

DEFAULT_MIEMBROS = 'Simétricos, sin cicatrices.Tono, trofismo, temperatura, sensibilidad ' \
                   'y movilidad conservada. Pulsos periféricos presentes, sin soplos. ' \
                   'No palpo adenopatías.'


class ExamenFisico(TimeStampedModel):
    impresion_general = models.TextField(verbose_name=u'Impresión General',
                                         blank=True, null=True,
                                         default=DEFAULT_IMPRESION_GENERAL)
    signos_vitales = models.TextField(verbose_name=u'Signos Vitales P.A.F.C.F.R Peso',
                                      blank=True, null=True)
    cabeza_cuello = models.TextField(verbose_name=u'Cabeza y Cuello',
                                     blank=True, null=True,
                                     default=DEFAULT_CABEZA_CUELLO)
    torax = models.TextField(verbose_name=u'Tórax', blank=True, null=True,
                             default=DEFAULT_TORAX)
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio', blank=True, null=True)
    cardiovascular = models.TextField(verbose_name=u'Ap. Cardiovascular',
                                      blank=True, null=True, default=DEFAULT_CARDIOVASCULAR)
    abdomen = models.TextField(verbose_name=u'Abdomen', blank=True, null=True,
                               default=DEFAULT_ABDOMEN)
    miembros = models.TextField(verbose_name=u'Miembros', blank=True, null=True,
                                default=DEFAULT_MIEMBROS)
    genitales = models.TextField(verbose_name=u'Genitales', blank=True, null=True)
    examen_neurologico = models.TextField(verbose_name=u'Exámen Neurológico', blank=True, null=True)
    fondo_ojos = models.TextField(verbose_name=u'Fondo de Ojos', blank=True, null=True)
    examen_proctologico = models.TextField(verbose_name=u'Exámen Proctológico',
                                           blank=True, null=True,
                                           default=DEFAULT_EXAMEN_PROCTOCOLOGICO)
