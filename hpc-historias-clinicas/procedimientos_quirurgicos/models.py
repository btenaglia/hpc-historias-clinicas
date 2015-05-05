# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ..core.models import TimeStampedModel


class ProcedimientosQuirurgicos(TimeStampedModel):
    """
    Procedimientos quirurgicos, los mismo serán
    utilizados para la carga de fojas quirurgicas
    """
    nombre = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name=u'Nombre del procedimiento')
    descripcion = models.TextField(blank=True, null=True,
                                   verbose_name=u'Descripción')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('procedimientos_quirurgicos:list')
