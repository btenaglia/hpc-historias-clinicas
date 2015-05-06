# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class Habitos(TimeStampedModel):
    alcohol = models.CharField(blank=True, null=True, max_length=150, default=u'Ocacional')
    tabaco = models.CharField(blank=True, null=True, max_length=150, default=u'Niega')
    cafe = models.CharField(blank=True, null=True, verbose_name=u'Café',
                            max_length=150, default=u'Ocacional')
    dieta = models.CharField(blank=True, null=True, max_length=150, default=u'Variada')
    drogadiccion = models.CharField(blank=True, null=True,
                                    verbose_name=u'Drogadicción',
                                    max_length=150,
                                    default=u'Niega')
    sueno = models.CharField(blank=True, null=True,
                             verbose_name=u'Sueño', max_length=150,
                             default=u'Conservado')
    sexualidad = models.CharField(blank=True, null=True, max_length=150, default=u'Heterosexual')
    medicamentos = models.TextField(blank=True, null=True, default=u'Niega')
    catarsis = models.CharField(blank=True, null=True, max_length=150, default=u'Conservada')
    diuresis = models.CharField(blank=True, null=True, max_length=150, default=u'Conservada')
    peso = models.FloatField(blank=True, null=True, max_length=150)
    talla = models.FloatField(blank=True, null=True, max_length=150)
