# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/inicio.html'),
        name="home"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("hpc-historias-clinicas.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Medicos
    url(r'^medicos/', include("hpc-historias-clinicas.medicos.urls", namespace="medicos")),
    # Ayudantes
    url(r'^ayudantes/', include("hpc-historias-clinicas.ayudantes.urls", namespace="ayudantes")),
    # Pacientes
    url(r'^pacientes/', include("hpc-historias-clinicas.pacientes.urls", namespace="pacientes")),
    # Historias clínicas
    url(r'^historias', include("hpc-historias-clinicas.historias.urls", namespace="historias")),
    # Diagnosticos
    url(r'^diagnosticos', include("hpc-historias-clinicas.diagnosticos.urls", namespace="diagnosticos")),
    # Motivos
    url(r'^motivos', include("hpc-historias-clinicas.anamnesis.urls", namespace="motivos")),
    # Inter consultas
    url(r'^inter/consultas', include("hpc-historias-clinicas.inter_consultas.urls", namespace="inter_consultas")),
    # Evoluciones
    url(r'^evoluciones', include("hpc-historias-clinicas.evoluciones.urls", namespace="evoluciones")),
    # Fojas Quirurgicas
    url(r'^fojas/quirurgicas', include("hpc-historias-clinicas.fojas_quirurgicas.urls", namespace="fojas_quirurgicas")),
    # Reportes
    url(r'^reportes', include("hpc-historias-clinicas.reportes.urls", namespace="reportes")),
    # Procedimiento quirurgicos
    url(r'^procedimientos/quirurgicos', include("hpc-historias-clinicas.procedimientos_quirurgicos.urls", namespace="procedimientos_quirurgicos")),
    # Epicrisis
    url(r'^epicrisis', include("hpc-historias-clinicas.epicrisis.urls", namespace="epicrisis")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
