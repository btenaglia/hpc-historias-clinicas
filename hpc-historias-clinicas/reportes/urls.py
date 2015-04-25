# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ReporteEvolucion, ReporteInterConsulta, ReporteHistoriaClinica

urlpatterns = patterns('',

    url(r'^/historia/(?P<pk>\d+)$', ReporteHistoriaClinica.as_view(), name='evolucion'),
    url(r'^/evolucion/(?P<pk>\d+)$', ReporteEvolucion.as_view(), name='evolucion'),
    url(r'^/inter/consultas/(?P<pk>\d+)$', ReporteInterConsulta.as_view(), name='inter_consultas'),

)


