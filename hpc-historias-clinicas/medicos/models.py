# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ..core.models import TimeStampedModel


class Medicos(TimeStampedModel):
    """
    Medicos de la institucion
    """
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    dni = models.IntegerField(max_length=8, blank=False, null=False, unique=True)
    foto = ThumbnailerImageField(blank=True, null=True, verbose_name=u"Foto del médico",
                                 upload_to="medicos_fotos")


    def get_absolute_url(self):
        return reverse('medicos:list')

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido
