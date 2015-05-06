# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class AntecedentesPersonales(TimeStampedModel):
    enfermedad_infantil = models.TextField(default=u'Niega', blank=True, null=True)
    enfermedad_adulto = models.TextField(default=u'Niega', blank=True, null=True)
    alergia = models.TextField(default=u'Niega', blank=True, null=True)
    antecedentes_traumaticos = models.TextField(default=u'Niega',
                                                verbose_name=u'Antecedentes Traumáticos',
                                                blank=True, null=True)
    antecedentes_quirurgicos = models.TextField(default=u'Niega cirugías previas',
                                                verbose_name=u'Antecedentes Quirúrgicos',
                                                blank=True, null=True)
    internaciones_previas = models.TextField(default=u'Niega', blank=True, null=True)
