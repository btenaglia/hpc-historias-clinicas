# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (MotivosListView,
                    MotivosCreateView,
                    MotivosUpdateView,
                    MotivosDeleteView,
                    traer_enfermedad)

urlpatterns = patterns('',

    url(r'^$', MotivosListView.as_view(), name='list'),
    url(r'^/create/$', MotivosCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)$', MotivosUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)$', MotivosDeleteView.as_view(), name='delete'),
    url(r'^/traer/enfermedad/$', traer_enfermedad, name='traer_enfermedad'),
)


