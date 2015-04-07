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


class PacientesCreateView(LoginRequiredMixin, CreateView):
    """
    Crear un nuevo paciente
    """
    model = Pacientes
    success_msg = 'El paciente se créo correctamente, ahora agregue una historia clínica'

    def get_success_url(self):
        # -- redirigir a la pagina para crear una hist. clinica
        # -- si desean agregarla luego de crear el paciente
        if 'confirmar_mas_historia' in self.request.POST:
            ultimo_paciente = Pacientes.objects.latest('id')
            self.success_url = '/historias/create/%s' % str(ultimo_paciente.id)

        messages.success(self.request, self.success_msg)
        return super(PacientesCreateView, self).get_success_url()


class PacientesUpdateView(LoginRequiredMixin, PacientesMixin, UpdateView):
    """
    Editar un paciente
    """
    model = Pacientes
    success_msg = 'El paciente se editó correctamente.'


class PacientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Pacientes
    success_url = '/pacientes/'
