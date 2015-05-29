from datetime import datetime
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from ..core.models import TimeStampedModel
from ..historias.models import Historias


class Evoluciones(TimeStampedModel):
    """
    Evoluciones de las historias clinicas
    """
    historia = models.ForeignKey(Historias, blank=False, null=False)
    fecha = models.DateField(blank=False, null=False, default=datetime.now())
    descripcion = models.TextField(blank=False, null=False)


class Fotos(TimeStampedModel):
    """
    Fotos de las evoluciones
    """
    evolucion = models.ForeignKey(Evoluciones)
    foto = ThumbnailerImageField(blank=False, null=False, upload_to='evoluciones_fotos')
    comentario = models.TextField(blank=True, null=True)