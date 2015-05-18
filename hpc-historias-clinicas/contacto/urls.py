# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import enviar_contacto

urlpatterns = patterns('',

    url(r'^$', enviar_contacto, name='enviar'),

)


