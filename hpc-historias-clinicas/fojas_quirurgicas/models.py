# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

from ..medicos.models import Medicos
from ..ayudantes.models import Ayudantes
from ..historias.models import Historias
from ..core.models import TimeStampedModel


class FojasQuirurgicas(TimeStampedModel):
    """
    Fojas Quirurgicas para las historias clínicas
    """
    historia = models.ForeignKey(Historias, blank=False, null=False)
    cirujano = models.ForeignKey(Medicos, blank=False, null=False)
    ayudante_1 = models.ForeignKey(Ayudantes, blank=False, null=False, verbose_name=u'1er Ayudante',
                                   related_name='ayudante_1')
    ayudante_2 = models.ForeignKey(Ayudantes, blank=False, null=False, verbose_name=u'2er Ayudante',
                                   related_name='ayudante_2')
    ayudante_3 = models.ForeignKey(Ayudantes, blank=False, null=False, verbose_name=u'3er Ayudante',
                                   related_name='ayudante_3')
    fecha = models.DateField(blank=False, null=False, default=datetime.now())
    hora_comienzo = models.TimeField(blank=False, null=False, verbose_name=u'Hora / Comienzo Operacón')
    hora_fin = models.TimeField(blank=False, null=False, verbose_name=u'Hora / Terminó Operacón')
