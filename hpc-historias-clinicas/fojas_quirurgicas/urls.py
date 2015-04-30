# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import FojasQuirurgicasListView

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', FojasQuirurgicasListView.as_view(), name='list'),

)



