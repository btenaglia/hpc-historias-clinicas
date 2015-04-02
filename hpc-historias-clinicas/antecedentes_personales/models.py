# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class AntecedentesPersonales(TimeStampedModel):
    enfermedad_infantil = models.TextField(default=u'Niega')
    enfermedad_adulto = models.TextField(default=u'Niega')
    alergia = models.TextField(default=u'Niega')
    antecedentes_traumaticos = models.TextField(default=u'Niega',
                                                verbose_name=u'Antecedentes Traumáticos')
    antecedentes_quirurgicos = models.TextField(default=u'Niega',
                                                verbose_name=u'Antecedentes Quirúrgicos')
    internaciones_previas = models.TextField(default=u'Niega')
