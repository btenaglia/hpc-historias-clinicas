# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import PacientesCreateView, PacientesListView, PacientesUpdateView, PacientesDeleteView

urlpatterns = patterns('',
    url(r'^$', PacientesListView.as_view(), name='list'),
    url(r'^create$', PacientesCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$', PacientesUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$', PacientesDeleteView.as_view(), name='delete'),

)


