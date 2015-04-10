# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import crear_historia, HistoriasListView, UbicacionCreateView, UbicacionUpdateView

urlpatterns = patterns('',

    url(r'^$', HistoriasListView.as_view(), name='list'),
    url(r'^/create/(?P<paciente>\d+)$', crear_historia, name='create'),
    url(r'^/ubicacion/create/(?P<historia>\d+)$', UbicacionCreateView.as_view(), name='ubicacion_create'),
    url(r'^/ubicacion/update/(?P<historia>\d+)$', UbicacionUpdateView.as_view(), name='ubicacion_update'),

)


