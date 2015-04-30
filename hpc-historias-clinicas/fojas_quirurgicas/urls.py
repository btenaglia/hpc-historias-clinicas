# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ( FojasQuirurgicasListView, 
	FojasQuirurgicasCreateView, 
	FojasQuirurgicasUpdateView, 
	FojasQuirurgicasDeleteView)

urlpatterns = patterns('',

    url(r'^/(?P<historia>\d+)$', FojasQuirurgicasListView.as_view(), name='list'),
    url(r'^/create/(?P<historia>\d+)$', FojasQuirurgicasCreateView.as_view(), name='create'),
    url(r'^/update/(?P<pk>\d+)/(?P<historia>\d+)$', FojasQuirurgicasUpdateView.as_view(), name='update'),
    url(r'^/delete/(?P<pk>\d+)/(?P<historia>\d+)$', FojasQuirurgicasDeleteView.as_view(), name='delete'),

)



