# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

from ..core.models import TimeStampedModel
from ..historias.models import Historias

DESCRIPCION_DEFAULT = 'Paciente de .... años de edad que cursa primer dia de ' \
                      'internación por cuadro de colecistitis aguda. Al examen ' \
                      'físico se encuentra lúcido, vigil y orientado globalmente. ' \
                      'Normotenso, afebril y hemodinamicamente estable con buena ' \
                      'mecánica respiratoria. Abdomen blando, depresible e indoloro. ' \
                      'RHA positivos. Antibioticoterapia con Ampicilina y Gentamicina.'


class Evoluciones(TimeStampedModel):
    historia = models.ForeignKey(Historias, blank=False, null=False)
    fecha = models.DateField(blank=False, null=False, default=datetime.now())
    descripcion = models.TextField(blank=False, null=False, default=DESCRIPCION_DEFAULT)