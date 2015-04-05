# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from braces.views import LoginRequiredMixin

from ..pacientes.models import Pacientes
from .models import Historias

from .forms import DiagnosticosModelForm


class HistoriasCreateView(LoginRequiredMixin, CreateView):
    model = Historias
    fields = ['tipo', 'fecha_ingreso', 'hora_ingreso']
    form_diagnostico = DiagnosticosModelForm

    def get_context_data(self, **kwargs):
        context = super(HistoriasCreateView, self).get_context_data(**kwargs)
        # -- para mostrar los datos de paciente
        context['paciente'] = get_object_or_404(Pacientes, id=self.kwargs['paciente'])

        context['form_diagnostico'] = self.form_diagnostico
        return context
