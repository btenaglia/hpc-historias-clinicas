# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel


class Planteos(TimeStampedModel):
    planteo = models.TextField(blank=True, null=True, verbose_name=u'Descripción')