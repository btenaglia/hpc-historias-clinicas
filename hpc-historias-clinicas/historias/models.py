# -*- coding: utf-8 -*-
import datetime
from django.db import models
from ..core.models import TimeStampedModel

from ..pacientes.models import Pacientes
from ..medicos.models import Medicos
from ..diagnosticos.models import Diagnosticos
from ..anamnesis.models import Anamnesis
from ..antecedentes_personales.models import AntecedentesPersonales
from ..habitos.models import Habitos
from ..antecedentes_familiares.models import AntecedentesFamiliares
from ..aparatos.models import Aparatos
from ..examen_fisico.models import ExamenFisico
from ..planteos.models import Planteos
from ..metodologias.models import Metodologias


class DptosCirugiaGeneral(TimeStampedModel):
    """
    Departamentos de cirugia general
    """
    nombre = models.CharField(blank=False, null=False, max_length=150)

    def __unicode__(self):
        return self.nombre


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

    paciente = models.ForeignKey(Pacientes, blank=False, null=False)
    medico = models.ForeignKey(Medicos, blank=False, null=False, verbose_name=u'Médico Responsable')
    dpto_cirugia = models.ForeignKey(DptosCirugiaGeneral, blank=False, null=False, verbose_name=u'Dpto. Cirugía')
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
    hora_ingreso = models.TimeField(blank=False, null=False,
                                    verbose_name=u"Hora de Ingreso",
                                    help_text=u'Formato: hh:mm',
                                    default=datetime.datetime.now())
    fecha_ingreso = models.DateField(blank=False, null=False, verbose_name=u"Fecha de Ingreso",
                                     help_text=u'Formato: dd/mm/yyyy',
                                     default=datetime.datetime.now())


class Ubicaciones(TimeStampedModel):
    SALAS = (
        ('SALA 1', 'SALA 1'),
        ('SALA 2', 'SALA 2'),
        ('SALA 3', 'SALA 3'),
        ('SALA 4', 'SALA 4'),
        ('SALA 5', 'SALA 5'),
        ('GAURDIA', 'GAURDIA'),
        ('NEO', 'NEO'),
        ('UTI', 'UTI'),
        ('UCO', 'UCO'),
        ('PRE PARTO', 'PRE PARTO'),
        ('CLARITA', 'CLARITA'),
        ('HOSPITAL DE DIA', 'HOSPITAL DE DIA'),

    )

    historia = models.ForeignKey(Historias, unique=True)
    sala = models.CharField(choices=SALAS, max_length=10, blank=False, null=False)
    cama = models.CharField(choices=( (str(x), x) for x in range(1, 33) ), max_length=2, blank=False, null=False)

    @classmethod
    def liberar_ubicacion(cls, historia_id):
        return cls.objects.filter(historia=historia_id).delete()

    class Meta:
        unique_together = ('sala', 'cama',)

