# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import (ReporteEvolucion,
                    ReporteInterConsulta,
                    ReporteHistoriaClinica,
                    ReporteFojaQuirurgica,
                    ReporteEpicrisis,
                    ReporteHistoriaClinicaPagina1,
                    ReporteHistoriaClinicaPagina3,
                    ReporteHistoriaClinicaPagina5,
                    ReporteHistoriaClinicaPagina7)

urlpatterns = patterns('',

    url(r'^/historia/(?P<pk>\d+)$', ReporteHistoriaClinica.as_view(), name='historia'),
    url(r'^/evolucion/(?P<pk>\d+)$', ReporteEvolucion.as_view(), name='evolucion'),
    url(r'^/inter/consultas/(?P<pk>\d+)$', ReporteInterConsulta.as_view(), name='inter_consultas'),
    url(r'^/foja/quirurgica/(?P<pk>\d+)$', ReporteFojaQuirurgica.as_view(), name='fojas_quirurgicas'),
    url(r'^/epicrisis/(?P<pk>\d+)$', ReporteEpicrisis.as_view(), name='epicrisis'),
    url(r'^/historia/clinica/(?P<pk>\d+)/page1$', ReporteHistoriaClinicaPagina1.as_view(), name='historia_p1'),
    url(r'^/historia/clinica/(?P<pk>\d+)/page3$', ReporteHistoriaClinicaPagina3.as_view(), name='historia_p3'),
    url(r'^/historia/clinica/(?P<pk>\d+)/page5$', ReporteHistoriaClinicaPagina5.as_view(), name='historia_p5'),
    url(r'^/historia/clinica/(?P<pk>\d+)/page7$', ReporteHistoriaClinicaPagina7.as_view(), name='historia_p7'),

)


