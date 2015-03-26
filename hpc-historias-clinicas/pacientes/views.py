# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin

from .models import Pacientes


class PacientesListView(LoginRequiredMixin, ListView):
    model = Pacientes


class PacientesCreateView(LoginRequiredMixin, CreateView):
    """
    Crear un nuevo paciente
    """
    model = Pacientes

    def get_success_url(self):
        messages.success(self.request, "El paciente se créo correctamente.")
        return super(PacientesCreateView, self).get_success_url()


class PacientesUpdateView(LoginRequiredMixin, UpdateView):
    """
    Editar un paciente
    """
    model = Pacientes

    def get_success_url(self):
        messages.success(self.request, "El paciente se editó correctamente.")
        return super(PacientesUpdateView, self).get_success_url()


class PacientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Pacientes
    success_url = '/pacientes'
