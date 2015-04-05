# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class Aparatos(TimeStampedModel):
    cardiovasculares = models.TextField(verbose_name=u'Ap. Cardiovasculares', blank=True, null=True)
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio', blank=True, null=True)
    digestivo = models.TextField(verbose_name=u'Ap. Digestivo', blank=True, null=True)
    urinario = models.TextField(verbose_name=u'Ap. Urinario', blank=True, null=True)
    genital = models.TextField(verbose_name=u'Ap. Genital', blank=True, null=True)
    locomotor = models.TextField(verbose_name=u'Ap. Locomotor', blank=True, null=True)
    sistema_nervioso = models.TextField(verbose_name=u'Sistema Nervioso', blank=True, null=True)
    sistema_endocrino = models.TextField(verbose_name=u'Sistema Endocrino', blank=True, null=True)
    piel_faneas = models.TextField(verbose_name=u'Piel y Faneas', blank=True, null=True)
    organos = models.TextField(verbose_name=u'Organos de los Sentidos', blank=True, null=True)