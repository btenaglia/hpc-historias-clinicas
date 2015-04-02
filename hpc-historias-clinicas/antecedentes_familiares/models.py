# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class AntecedentesFamiliares(TimeStampedModel):
    padre = models.CharField(blank=True, null=True, max_length=150)
    madre = models.CharField(blank=True, null=True, max_length=150)
    hermanos = models.CharField(blank=True, null=True, max_length=150)
    hijos = models.CharField(blank=True, null=True, max_length=150)
    otros = models.TextField(blank=True, null=True, max_length=150)
