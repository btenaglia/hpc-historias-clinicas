# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import AyudantesListView, AyudantesCreateView, AyudantesUpdateView, AyudantesDeleteView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=AyudantesListView.as_view(),
        name='ayudantes_list'
    ),
    url(r'^/create/$', AyudantesCreateView.as_view(), name='ayudantes_nuevo'),
    url(r'^/update/(?P<pk>\d+)$', AyudantesUpdateView.as_view(), name='ayudantes_update'),
    url(r'^/delete/(?P<pk>\d+)$', AyudantesDeleteView.as_view(), name='ayudantes_delete'),
)

