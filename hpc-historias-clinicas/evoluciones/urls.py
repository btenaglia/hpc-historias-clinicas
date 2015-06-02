# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (EvolucionesListView,
                    EvolucionesCreateView,
                    EvolucionesUpdateView,
                    EvolucionesDeleteView,
                    EvolucionesFotosListView,
                    EvolucionesFotosCreateView,
                    EvolucionesFotosUpdateView,
                    EvolucionesFotosDeleteView)

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', EvolucionesListView.as_view(), name='list'),
    url(r'^/create/(?P<historia>\d+)$', EvolucionesCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)/(?P<historia>\d+)$', EvolucionesUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)/(?P<historia>\d+)$', EvolucionesDeleteView.as_view(), name='delete'),
    url(r'^/fotos/(?P<evolucion>\d+)$', EvolucionesFotosListView.as_view(), name='fotos'),
    url(r'^/fotos/create/(?P<evolucion>\d+)$', EvolucionesFotosCreateView.as_view(), name='fotos_create'),
    url(r'^/fotos/update/(?P<pk>\d+)/(?P<evolucion>\d+)$', EvolucionesFotosUpdateView.as_view(), name='fotos_update'),
    url(r'^/fotos/delete/(?P<pk>\d+)/(?P<evolucion>\d+)$', EvolucionesFotosDeleteView.as_view(), name='fotos_delete'),

)



