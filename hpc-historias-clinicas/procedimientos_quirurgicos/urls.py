# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (ProcedimientosQuirurgicosListView,
                    ProcedimientosQuirurgicosCreateView,
                    ProcedimientosQuirurgicosUpdateView,
                    ProcedimientosQuirurgicosDeleteView,
                    traer_descripcion)

urlpatterns = patterns('',

    url(r'^$', ProcedimientosQuirurgicosListView.as_view(), name='list'),
    url(r'^/create/$', ProcedimientosQuirurgicosCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)$', ProcedimientosQuirurgicosUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)$', ProcedimientosQuirurgicosDeleteView.as_view(), name='delete'),
    url(r'^/traer/descripcion/$', traer_descripcion, name='traer_descripcion'),
)
