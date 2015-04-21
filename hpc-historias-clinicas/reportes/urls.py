# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ReporteEvolucion

urlpatterns = patterns('',

    url(r'^/evolucion/(?P<pk>\d+)$', ReporteEvolucion.as_view(), name='evolucion'),
)


