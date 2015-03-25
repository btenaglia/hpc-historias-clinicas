# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import Ayudantes


class AyudantesListView(LoginRequiredMixin, ListView):
    """
    Lista todos los ayudantes
    """
    model = Ayudantes


class AyudantesCreateView(LoginRequiredMixin, CreateView):
    """
    Creacion de medico
    """
    model = Ayudantes

    def get_success_url(self):
        messages.success(self.request, "El ayudante se agregó correctamente.")
        return super(AyudantesCreateView, self).get_success_url()


class AyudantesUpdateView(LoginRequiredMixin, UpdateView):
    """
    Modificacion de un ayudante
    """
    model = Ayudantes

    def get_success_url(self):
        messages.success(self.request, "El ayudante se editó correctamente.")
        return super(AyudantesUpdateView, self).get_success_url()


class AyudantesDeleteView(LoginRequiredMixin, DeleteView):
    """
    Eliminar un ayudante
    """
    model = Ayudantes
    success_url = '/ayudantes'