# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ..core.models import TimeStampedModel


class TipoDiagnosticos(TimeStampedModel):
    nombre = models.CharField(max_length=150, blank=False, null=False, verbose_name=u'Diagnóstico')

    def get_absolute_url(self):
        return reverse('diagnosticos:list')

    def __unicode__(self):
        return self.nombre


class Diagnosticos(TimeStampedModel):
    tipo_diagnostico = models.ForeignKey(TipoDiagnosticos, blank=True, null=True,
                                         verbose_name=u'Diagnóstico')
    descripcion = models.TextField(blank=True, null=True,
                                   help_text=u'Escriba una descripcion si lo considera útil')
    fecha = models.DateField(blank=False, null=False,
                             help_text=u'Formato: dd/mm/yyyy')
    hora = models.TimeField(blank=False, null=False,
                            help_text=u'Formato: hh:mm')
