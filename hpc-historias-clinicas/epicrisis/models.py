# -*- coding: utf-8 -*-
from django.db import models

from ..core.models import TimeStampedModel

from ..historias.models import Historias


class Epicrisis(TimeStampedModel):
    """
    - Tabla de la Epicrisis relacionada a la historia clinica
    - La epicrisis es un documento que se completa cuando
    se de de alta el paciente
    """
    historia = models.ForeignKey(Historias)
    equipo_referencia = models.CharField(max_length=150, blank=True, null=True,
                                         verbose_name=u"Equipo de referencia en la internación",
                                         default=u"Cirugía general")
    antecedentes = models.TextField(blank=True, null=True, verbose_name=u"Antecedentes")
    problemas = models.TextField(blank=True, null=True,
                                 verbose_name=u"Detalle de los problemas abordados en el proceso"
                                              u" actual")
    fecha_egreso = models.DateField(verbose_name=u"Fecha de egreso")
    diagnostico_egreso = models.TextField(blank=True, null=True, verbose_name=u"Diagnóstico de egreso")
    resultado_examenes = models.TextField(blank=True, null=True,
                                          verbose_name=u"Resultado de exámenes complementarios")
    laboratorio_alta = models.TextField(blank=True, null=True, verbose_name=u"Laboratorio al alta")
    tratamiento_alta = models.TextField(blank=True, null=True,
                                        verbose_name=u"Tratamiento al alta",
                                        default=u"Control por consultorio externo."
                                                u"Curaciones de la herida."
                                                u"Antibiótico terapia.")
    pendientes = models.TextField(blank=True, null=True,
                                  verbose_name=u"Pendientes de resolución en el proceso"
                                               u" de atención ambulatorio")
    equipo_referencia_alta = models.CharField(max_length=150, blank=True, null=True,
                                              verbose_name=u"Equipo y centro de referencia al alta",
                                              default=u"Cirugía general, Otro")
    fecha_proxima_consulta = models.DateField(verbose_name=u"Fecha de la próxima consulta")
    hora_proxima_consulta = models.TimeField(verbose_name=u"Hora de la próxima consulta")



