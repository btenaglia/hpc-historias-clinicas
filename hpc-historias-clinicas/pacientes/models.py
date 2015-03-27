# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from ..core.models import TimeStampedModel


class Pacientes(TimeStampedModel):
    """
    Pacientes del Hospital
    """

    SEXOS = (
        (0, 'Masculino'),
        (1, 'Femenino'),
    )
    ESTADO_CIVIL = (
        (0, 'Soltero'),
        (1, 'Casado'),
        (2, 'Viudo'),
        (3, 'Divorciado'),
    )

    apellido = models.CharField(blank=False, null=False, max_length=100)
    nombre = models.CharField(blank=False, null=False, max_length=100)
    sexo = models.IntegerField(choices=SEXOS, blank=False, null=False, max_length=1)
    madre = models.CharField(max_length=300, verbose_name=u"Nombre y Apellido de la madre")
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    domicilio_numero = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"Número de domicilio")
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(max_length=3, blank=True, null=True, default=0)
    fecha_nacimiento = models.DateField(verbose_name=u"Fecha de Nacimiento", blank=False, null=False, help_text=u'Formato: dd/mm/yyyy')
    documento = models.CharField(max_length=8, blank=True, null=True)
    estado_civil = models.IntegerField(choices=ESTADO_CIVIL, blank=False, null=False)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    procedencia = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    obra_social = models.CharField(max_length=100, blank=True, null=True)
    numero_afiliado = models.CharField(max_length=100, blank=True, null=True)
    hora_ingreso = models.TimeField(blank=False, null=False, verbose_name=u"Hora de Ingreso", help_text=u'Formato: hh:mm')
    fecha_ingreso = models.DateField(blank=False, null=False, verbose_name=u"Fecha de Ingreso", help_text=u'Formato: dd/mm/yyyy')

    def get_absolute_url(self):
        return reverse('pacientes:list')
