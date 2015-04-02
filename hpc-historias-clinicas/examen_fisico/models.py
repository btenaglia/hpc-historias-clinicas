# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class ExamenFisico(TimeStampedModel):
    impresion_general = models.TextField(verbose_name=u'Impresión General')
    signos_vitales = models.TextField(verbose_name=u'Signos Vitales P.A.F.C.F.R Peso Cabez y Cuello')
    torax = models.TextField(verbose_name=u'Torax')
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio')
    cardiovascular = models.TextField(verbose_name=u'Ap. Cardiovascular')
    abdomen = models.TextField(verbose_name=u'Abdomen')
    miembros = models.TextField(verbose_name=u'Miembros')
    genitales = models.TextField(verbose_name=u'Genitales')
    examen_neurologico = models.TextField(verbose_name=u'Exámen Neurológico')
    fondo_ojos = models.TextField(verbose_name=u'Fondo de Ojos')
    examen_proctologico = models.TextField(verbose_name=u'Exámen Proctológico')
