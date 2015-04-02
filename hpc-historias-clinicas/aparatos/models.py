# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class Aparatos(TimeStampedModel):
    cardiovasculares = models.TextField(verbose_name=u'Ap. Cardiovasculares')
    respiratorio = models.TextField(verbose_name=u'Ap. Respiratorio')
    digestivo = models.TextField(verbose_name=u'Ap. Digestivo')
    urinario = models.TextField(verbose_name=u'Ap. Urinario')
    genital = models.TextField(verbose_name=u'Ap. Genital')
    locomotor = models.TextField(verbose_name=u'Ap. Locomotor')
    sistema_nervioso = models.TextField(verbose_name=u'Sistema Nervioso')
    sistema_endocrino = models.TextField(verbose_name=u'Sistema Endocrino')
    piel_faneas = models.TextField(verbose_name=u'Piel y Faneas')
    organos = models.TextField(verbose_name=u'Organos de los Sentidos')