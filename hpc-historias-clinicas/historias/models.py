# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import TimeStampedModel

from ..pacientes.models import Pacientes
from ..diagnosticos.models import Diagnosticos
from ..anamnesis.models import Anamnesis
from ..antecedentes_personales.models import AntecedentesPersonales
from ..habitos.models import Habitos
from ..antecedentes_familiares.models import AntecedentesFamiliares
from ..aparatos.models import Aparatos
from ..examen_fisico.models import ExamenFisico
from ..planteos.models import Planteos
from ..metodologias.models import Metodologias


class Historias(TimeStampedModel):
    TIPO = (
        (1, 'Internación'),
        (2, 'Inter Consulta'),
    )

    ESTADO = (
        (1, 'Alta'),
        (2, 'Óbito'),
        (3, 'Pase de servicio'),
    )
    paciente = models.OneToOneField(Pacientes, blank=False, null=False)
    codigo = models.CharField(blank=False, null=False, max_length=10)
    tipo = models.IntegerField(choices=TIPO, default=1, blank=False, null=False)
    estado = models.IntegerField(choices=ESTADO, blank=True, null=True)
    diagnostico = models.OneToOneField(Diagnosticos, blank=False, null=False)
    anamnesis = models.OneToOneField(Anamnesis, blank=False, null=False)
    antecedentes_personales = models.OneToOneField(AntecedentesPersonales, blank=False, null=False)
    habitos = models.OneToOneField(Habitos, blank=False, null=False)
    antecedentes_familiares = models.OneToOneField(AntecedentesFamiliares, blank=False, null=False)
    aparatos = models.OneToOneField(Aparatos, blank=False, null=False)
    examen_fisico = models.OneToOneField(ExamenFisico, blank=False, null=False)
    planteos = models.OneToOneField(Planteos, blank=False, null=False)
    metodologias = models.OneToOneField(Metodologias, blank=False, null=False)

