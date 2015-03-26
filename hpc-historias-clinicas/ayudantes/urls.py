# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import AyudantesListView, AyudantesCreateView, AyudantesUpdateView, AyudantesDeleteView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=AyudantesListView.as_view(),
        name='list'
    ),
    url(r'^create$', AyudantesCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$', AyudantesUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$', AyudantesDeleteView.as_view(), name='delete'),
)

