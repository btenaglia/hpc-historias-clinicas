# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import crear_historia, HistoriasListView, UbicacionCreateView

urlpatterns = patterns('',

    url(r'^$', HistoriasListView.as_view(), name='list'),
    url(r'^/create/(?P<paciente>\d+)$', crear_historia, name='create'),
    url(r'^/ubicacion/create/(?P<historia>\d+)$', UbicacionCreateView.as_view(), name='ubicacion_create'),

)


