# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import InterConsultasListView, InterConsultasCreateView, InterConsultasUpdateView, InterConsultasDeleteView

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', InterConsultasListView.as_view(), name='list'),
    url(r'^/create/(?P<historia>\d+)$', InterConsultasCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)/(?P<historia>\d+)$', InterConsultasUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)/(?P<historia>\d+)$', InterConsultasDeleteView.as_view(), name='delete'),

)



