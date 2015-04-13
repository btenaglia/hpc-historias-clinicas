from django.shortcuts import render
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import InterConsultas
from ..historias.models import Historias


class InterConsultasListView(LoginRequiredMixin, ListView):
    """
    Obtengo las inter-consultas de una historia clinica
    """
    model = InterConsultas

    def get_context_data(self, **kwargs):
        """Es necesario traer los datos de la historia clinica"""
        ctx = super(InterConsultasListView, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_queryset(self):
        return InterConsultas.objects.filter(historia=self.kwargs['historia'])
