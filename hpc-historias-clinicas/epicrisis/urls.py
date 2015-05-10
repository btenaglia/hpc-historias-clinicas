# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import EpicrisisCreateView, EpicrisisUpdateView

urlpatterns = patterns('',

    url(r'^/create/(?P<historia>\d+)$', EpicrisisCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)/(?P<historia>\d+)$', EpicrisisUpdateView.as_view(), name='update'),

)




