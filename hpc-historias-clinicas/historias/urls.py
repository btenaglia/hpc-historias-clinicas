# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import crear_historia

urlpatterns = patterns('',
    url(r'^create/(?P<paciente>\d+)$', crear_historia, name='create'),

)


