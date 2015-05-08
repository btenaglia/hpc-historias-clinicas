# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel
from ..historias.models import Historias


class TipoMetodologias(TimeStampedModel):
    nombre = models.CharField(max_length=150, blank=False, null=False, verbose_name=u'Metodología')

    def __unicode__(self):
        return self.nombre


class Metodologias(TimeStampedModel):
    """
    Metodologías: una historia clinica puede tener muchas metodologías
    """
    tipo_metodologia = models.ForeignKey(TipoMetodologias, blank=True, null=True,
                                         verbose_name=u'Metodología')
    historia = models.ForeignKey(Historias, blank=True, null=True)