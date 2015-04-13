# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import InterConsultas
from ..historias.models import Historias


class InterConsultasMixin(object):

    def success_msg(self):
        return NotImplemented

    def get_context_data(self, **kwargs):
        """Es necesario traer los datos de la historia clinica"""
        ctx = super(InterConsultasMixin, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/inter/consultas/%s' % (self.kwargs['historia'])


class InterConsultasListView(LoginRequiredMixin, InterConsultasMixin, ListView):
    """
    Obtengo las inter-consultas de una historia clinica
    """
    model = InterConsultas

    def get_queryset(self):
        return InterConsultas.objects.filter(historia=self.kwargs['historia'])


class InterConsultasCreateView(LoginRequiredMixin, InterConsultasMixin, CreateView):
    """ Creacion de una inter consulta """
    model = InterConsultas
    fields = ['fecha', 'descripcion']
    success_msg = 'La inter consulta se agregó con éxito.'

    def post(self, request, *args, **kwargs):
        # -- Es necesario indicarle el Id de la historia
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = None

        form.instance.historia_id = self.kwargs['historia']
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class InterConsultasUpdateView(LoginRequiredMixin, InterConsultasMixin, UpdateView):
    """ Edicion de una inter consulta """
    model = InterConsultas
    fields = ['fecha', 'descripcion']
    success_msg = 'La inter consulta se editó con éxito.'


class InterConsultasDeleteView(LoginRequiredMixin, InterConsultasMixin, DeleteView):
    """ Eliminar una inter consulta """
    model = InterConsultas
    success_msg = 'La inter consulta se eliminó con éxito.'