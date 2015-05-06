# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel

DEFAULT_AP_CARDIOVASCULAR = 'Niega hipertensión, hipotensión, precordialgias, ' \
                            'palpitaciones, disnea de esfuerzo, disnea de reposo, ' \
                            'disnea paroxística noctura, ortopnea, claudicación intermitente, ' \
                            'cianosis, edemas, varices. Foco para Chagas negativo'

DEFAULT_AP_RESPIRATORIO = 'Niega: tos, expectoración, dolor toraxico, asma, broncoespasmo,' \
                          'neumonía, hemoptisis, vómica, derrame pleural. Foco para tuberculosis ' \
                          'negativo'

DEFAULT_AP_URINARIO = 'Niega: disuria, polaquiuria, poliurja, hematuria, piuria, litiasis urinaria, ' \
                      'cólico renal, pujos y tenesmo vesical, infecciones urinarias o repetición.'

DEFAULT_AP_GENITAL = 'Menarca:  años, FUM: hace   años, Gestas: / Paras:  , niega ' \
                     'anticoncepción, flujo vaginal, metrorragias, nodulos mamarios ' \
                     'secreción por el pezón'

DEFAULT_SIST_NERVIOSO = 'Niega: cefaleas, mareos, epilepsia, convulsiones, pérdida de ' \
                        'conocimiento, y otros trastornos  sensoriales, sensitivos y motores.'

DEFAULT_SIST_ENDOCRINO = 'Niega: diabetes y otrasendocrinopatías'

DEFAULT_AP_DIGESTIVOS = 'Niega disfagia, disglusia, odinofagia, pirosis, ardor epigastrico, '\
                        'nauseas, vomitos, hematemesis, melena enterorragia proctorragia, ' \
                        'cambio en el habito evacuatorio, pujos y tenesmo rectal, ictericia '\
                        'coluria y acolia, hepatitis y parasitosis.'


class Aparatos(TimeStampedModel):
    cardiovasculares = models.TextField(verbose_name=u'Ap. Cardiovasculares',
                                        blank=True, null=True,
                                        default=DEFAULT_AP_CARDIOVASCULAR)
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio',
                                    blank=True, null=True,
                                    default=DEFAULT_AP_RESPIRATORIO)
    digestivo = models.TextField(verbose_name=u'Ap. Digestivo',
                                 blank=True, null=True,
                                 default=DEFAULT_AP_DIGESTIVOS)
    urinario = models.TextField(verbose_name=u'Ap. Urinario',
                                blank=True, null=True,
                                default=DEFAULT_AP_URINARIO)
    genital = models.TextField(verbose_name=u'Ap. Genital', blank=True, null=True,
                               default=DEFAULT_AP_GENITAL)
    locomotor = models.TextField(verbose_name=u'Ap. Locomotor', blank=True, null=True,
                                 default=u'Sin particularidades')
    sistema_nervioso = models.TextField(verbose_name=u'Sistema Nervioso',
                                        blank=True, null=True,
                                        default=DEFAULT_SIST_NERVIOSO)
    sistema_endocrino = models.TextField(verbose_name=u'Sistema Endocrino',
                                         blank=True, null=True,
                                         default=DEFAULT_SIST_ENDOCRINO)
    piel_faneas = models.TextField(verbose_name=u'Piel y Faneas',
                                   blank=True, null=True,
                                   default=u'Sin particularidades')
    organos = models.TextField(verbose_name=u'Organos de los Sentidos',
                               blank=True, null=True,
                               default=u'Sin particularidades')