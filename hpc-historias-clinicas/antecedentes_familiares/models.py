# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class AntecedentesFamiliares(TimeStampedModel):
    padre = models.CharField(blank=True, null=True, max_length=150, default=u'Vivo, Sano')
    madre = models.CharField(blank=True, null=True, max_length=150, default=u'Viva, Sana')
    hermanos = models.CharField(blank=True, null=True, max_length=150, default=u'Niega')
    hijos = models.CharField(blank=True, null=True, max_length=150, default=u'Niega')
    otros = models.TextField(blank=True, null=True, max_length=150,
                             default=u'Niega enfermedadase heredogenéticas')
