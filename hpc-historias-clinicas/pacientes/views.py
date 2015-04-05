# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin

from .models import Pacientes


class PacientesMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(PacientesMixin, self).get_success_url()


class PacientesListView(LoginRequiredMixin, ListView):
    model = Pacientes


class PacientesCreateView(LoginRequiredMixin, PacientesMixin, CreateView):
    """
    Crear un nuevo paciente
    """
    model = Pacientes
    success_msg = 'El paciente se créo correctamente.'

    def form_valid(self, form):
        # si quieren dirigirse a agregar una nueva Historia,
        # necesito obtener el ultimo paciente agregado
        if 'confirmar_mas_historia' in self.request.POST:
            lastId = Pacientes.objects.latest('id')
            self.success_url = '/historias/create/%s' % str(lastId.id)

        return super(PacientesCreateView, self).form_valid(form)


class PacientesUpdateView(LoginRequiredMixin, PacientesMixin, UpdateView):
    """
    Editar un paciente
    """
    model = Pacientes
    success_msg = 'El paciente se editó correctamente.'


class PacientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Pacientes
    success_url = '/pacientes/'
