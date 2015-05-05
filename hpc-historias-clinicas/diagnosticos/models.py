# -*- coding: utf-8 -*-
from datetime import datetime
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
    fecha = models.DateField(blank=False, null=False,
                             help_text=u'Formato: dd/mm/yyyy',
                             default=datetime.now())
    hora = models.TimeField(blank=False, null=False,
                            help_text=u'Formato: hh:mm', default=datetime.now())
