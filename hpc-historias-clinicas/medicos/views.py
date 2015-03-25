# -*- coding: utf-8 -*-

from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Medicos


class MedicosListView(LoginRequiredMixin, ListView):
    """
    Lista todos los medicos
    """
    model = Medicos


class MedicosCreateView(LoginRequiredMixin, CreateView):
    """
    Creacion de medico
    """
    model = Medicos

    def get_success_url(self):
        messages.success(self.request, 'El médico se agregó correctamente.')
        return super(MedicosCreateView, self).get_success_url()


class MedicosUpdateView(LoginRequiredMixin, UpdateView):
    """
    Modificacion de un medico
    """
    model = Medicos

    def get_success_url(self):
        messages.success(self.request, 'El médico se editó correctamente.')
        return super(MedicosUpdateView, self).get_success_url()


class MedicosDeleteView(LoginRequiredMixin, DeleteView):
    """
    Eliminar un medico
    """
    model = Medicos
    success_url = '/medicos'
