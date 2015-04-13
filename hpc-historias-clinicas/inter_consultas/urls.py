# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import InterConsultasListView

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', InterConsultasListView.as_view(), name='list'),

)



