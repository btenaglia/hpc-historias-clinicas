# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from braces.views import LoginRequiredMixin

from ..pacientes.models import Pacientes
from .models import Historias

from .forms import (DiagnosticosModelForm,
                    AnamnesisModelForm,
                    AntecedentesPersonalesModelForm,
                    HabitosModelForm,
                    AntecedentesFamiliaresModelForm,
                    AparatosModelForm,
                    ExamenFisicoModelForm,
                    PlanteosModelForm,
                    MetodologiasModelForm)


class HistoriasCreateView(LoginRequiredMixin, CreateView):
    model = Historias
    fields = ['tipo', 'fecha_ingreso', 'hora_ingreso']
    form_diagnostico = DiagnosticosModelForm

    def get_context_data(self, **kwargs):
        context = super(HistoriasCreateView, self).get_context_data(**kwargs)
        # -- para mostrar los datos de paciente
        context['paciente'] = get_object_or_404(Pacientes, id=self.kwargs['paciente'])
        # -- formularios
        context['form_diagnostico'] = DiagnosticosModelForm
        context['form_anamnesis'] = AnamnesisModelForm
        context['form_antecedentes_personales'] = AntecedentesPersonalesModelForm
        context['form_habitos'] = HabitosModelForm
        context['form_antecedentes_familiares'] = AntecedentesFamiliaresModelForm
        context['form_aparatos'] = AparatosModelForm
        context['form_examen_fisico'] = ExamenFisicoModelForm
        context['form_planteos'] = PlanteosModelForm
        context['form_metodologias'] = MetodologiasModelForm
        return context
