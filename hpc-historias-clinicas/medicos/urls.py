# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import MedicosListView, MedicosCreateView, MedicosUpdateView, MedicosDeleteView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=MedicosListView.as_view(),
        name='medicos_list'
    ),
    url(r'^/create/$', MedicosCreateView.as_view(), name='medicos_nuevo'),
    url(r'^/update/(?P<pk>\d+)$', MedicosUpdateView.as_view(), name='medicos_update'),
    url(r'^/delete/(?P<pk>\d+)$', MedicosDeleteView.as_view(), name='medicos_delete'),
)

