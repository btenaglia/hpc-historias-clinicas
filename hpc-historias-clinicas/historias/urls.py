# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import HistoriasCreateView

urlpatterns = patterns('',
    url(r'^create/(?P<paciente>\d+)$', HistoriasCreateView.as_view(), name='create'),

)


