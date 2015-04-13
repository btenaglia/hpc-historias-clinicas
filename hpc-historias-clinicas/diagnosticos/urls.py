# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (TipoDiagnosticosListView,
                    TipoDiagnosticosCreateView,
                    TipoDiagnosticosUpdateView,
                    TipoDiagnosticosDeleteView)

urlpatterns = patterns('',

    url(r'^$', TipoDiagnosticosListView.as_view(), name='list'),
    url(r'^/create/$', TipoDiagnosticosCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)$', TipoDiagnosticosUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)$', TipoDiagnosticosDeleteView.as_view(), name='delete'),

)


