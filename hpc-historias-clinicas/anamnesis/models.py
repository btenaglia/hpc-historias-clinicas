# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ..core.models import TimeStampedModel


class MotivosConsultas(TimeStampedModel):
    motivo = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name=u'Motivo de consulta')

    def __unicode__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('motivos:list')


class Anamnesis(TimeStampedModel):
    motivo_consulta = models.ForeignKey(MotivosConsultas, blank=True, null=True,
                                        verbose_name=u'Motivo de consulta')
    enfermedad_actual = models.TextField(blank=True, null=True,
                                   help_text=u'Enfermedad actual')