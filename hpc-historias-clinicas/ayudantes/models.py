from django.core.urlresolvers import reverse
from django.db import models
from ..core.models import TimeStampedModel


class Ayudantes(TimeStampedModel):
    """
    Medicos ayudantes de la institucion
    """
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    dni = models.IntegerField(max_length=8, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('ayudantes:ayudantes_list')

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido