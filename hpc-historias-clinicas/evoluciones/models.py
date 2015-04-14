from django.db import models

from ..core.models import TimeStampedModel
from ..historias.models import Historias


class Evoluciones(TimeStampedModel):
    historia = models.ForeignKey(Historias, blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)