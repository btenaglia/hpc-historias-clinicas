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


class MedicosMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(MedicosMixin, self).get_success_url()


class MedicosListView(LoginRequiredMixin, ListView):
    """
    Lista todos los medicos
    """
    model = Medicos


class MedicosCreateView(LoginRequiredMixin, MedicosMixin, CreateView):
    """
    Creacion de medico
    """
    model = Medicos
    success_msg = 'El médico se agregó correctamente.'


class MedicosUpdateView(LoginRequiredMixin, MedicosMixin, UpdateView):
    """
    Modificacion de un medico
    """
    model = Medicos
    success_msg = 'El médico se editó correctamente.'


class MedicosDeleteView(LoginRequiredMixin, DeleteView):
    """
    Eliminar un medico
    """
    model = Medicos
    success_url = '/medicos/'
