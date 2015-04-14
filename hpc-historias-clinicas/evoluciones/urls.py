# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import EvolucionesListView, EvolucionesCreateView, EvolucionesUpdateView, EvolucionesDeleteView

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', EvolucionesListView.as_view(), name='list'),
    url(r'^/create/(?P<historia>\d+)$', EvolucionesCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)/(?P<historia>\d+)$', EvolucionesUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)/(?P<historia>\d+)$', EvolucionesDeleteView.as_view(), name='delete'),

)



