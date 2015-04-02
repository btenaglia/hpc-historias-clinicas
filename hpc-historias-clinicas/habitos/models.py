# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class Habitos(TimeStampedModel):
    alcohol = models.CharField(blank=True, null=True, max_length=150)
    tabaco = models.CharField(blank=True, null=True, max_length=150)
    cafe = models.CharField(blank=True, null=True, verbose_name=u'Café',
                            max_length=150)
    dieta = models.CharField(blank=True, null=True, max_length=150)
    drogadiccion = models.CharField(blank=True, null=True,
                                    verbose_name=u'Drogadicción', max_length=150)
    sueno = models.CharField(blank=True, null=True,
                             verbose_name=u'Sueño', max_length=150)
    medicamentos = models.TextField(blank=True, null=True)
    catarsis = models.CharField(blank=True, null=True, max_length=150)
    diuresis = models.CharField(blank=True, null=True, max_length=150)
    peso = models.FloatField(blank=True, null=True, max_length=150)
    talla = models.FloatField(blank=True, null=True, max_length=150)
