# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class ExamenFisico(TimeStampedModel):
    impresion_general = models.TextField(verbose_name=u'Impresión General', blank=True, null=True)
    signos_vitales = models.TextField(verbose_name=u'Signos Vitales P.A.F.C.F.R Peso Cabeza y Cuello',
                                      blank=True, null=True)
    torax = models.TextField(verbose_name=u'Torax', blank=True, null=True)
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio', blank=True, null=True)
    cardiovascular = models.TextField(verbose_name=u'Ap. Cardiovascular', blank=True, null=True)
    abdomen = models.TextField(verbose_name=u'Abdomen', blank=True, null=True)
    miembros = models.TextField(verbose_name=u'Miembros', blank=True, null=True)
    genitales = models.TextField(verbose_name=u'Genitales', blank=True, null=True)
    examen_neurologico = models.TextField(verbose_name=u'Exámen Neurológico', blank=True, null=True)
    fondo_ojos = models.TextField(verbose_name=u'Fondo de Ojos', blank=True, null=True)
    examen_proctologico = models.TextField(verbose_name=u'Exámen Proctológico', blank=True, null=True)
