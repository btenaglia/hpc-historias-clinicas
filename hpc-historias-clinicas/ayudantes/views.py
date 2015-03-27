# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import Ayudantes


class AyudantesMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(AyudantesMixin, self).get_success_url()


class AyudantesListView(LoginRequiredMixin, ListView):
    """
    Lista todos los ayudantes
    """
    model = Ayudantes


class AyudantesCreateView(LoginRequiredMixin, AyudantesMixin, CreateView):
    """
    Creacion de medico
    """
    model = Ayudantes
    success_msg = 'El ayudante se agregó correctamente.'


class AyudantesUpdateView(LoginRequiredMixin, AyudantesMixin, UpdateView):
    """
    Modificacion de un ayudante
    """
    model = Ayudantes
    success_msg = 'El ayudante se editó correctamente.'


class AyudantesDeleteView(LoginRequiredMixin, DeleteView):
    """
    Eliminar un ayudante
    """
    model = Ayudantes
    success_url = '/ayudantes'