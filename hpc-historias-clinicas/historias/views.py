# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template import defaultfilters
from ..pacientes.models import Pacientes
from .forms import (DiagnosticosModelForm,
                    AnamnesisModelForm,
                    AntecedentesPersonalesModelForm,
                    HabitosModelForm,
                    AntecedentesFamiliaresModelForm,
                    AparatosModelForm,
                    ExamenFisicoModelForm,
                    PlanteosModelForm,
                    MetodologiasModelForm,
                    HistoriasModelForm)


@login_required(redirect_field_name='accounts/login/')
def crear_historia(request, paciente):
    ctx = {
        'paciente': get_object_or_404(Pacientes, id=paciente),
        'form_historia': HistoriasModelForm(prefix='historia'),
        'form_diagnostico': DiagnosticosModelForm(prefix='diagnostico'),
        'form_anamnesis': AnamnesisModelForm(prefix='anamnesis'),
        'form_antecedentes_personales': AntecedentesPersonalesModelForm(prefix='antecedentes_personales'),
        'form_habitos': HabitosModelForm(prefix='habitos'),
        'form_antecedentes_familiares': AntecedentesFamiliaresModelForm(prefix='antecedentes_familiares'),
        'form_aparatos': AparatosModelForm(prefix='aparatos'),
        'form_examen_fisico': ExamenFisicoModelForm(prefix='examen_fisico'),
        'form_planteos': PlanteosModelForm(prefix='planteos'),
        'form_metodologias': MetodologiasModelForm(prefix='metodologias')
    }

    if request.method == "POST":
        form_historia = HistoriasModelForm(request.POST, prefix='historia')
        form_diagnostico = DiagnosticosModelForm(request.POST, prefix='diagnostico')
        form_anamnesis = AnamnesisModelForm(request.POST, prefix='anamnesis')
        form_antecedentes_personales = AntecedentesPersonalesModelForm(request.POST, prefix='antecedentes_personales')
        form_habitos = HabitosModelForm(request.POST, prefix='habitos')
        form_antecedentes_familiares = AntecedentesFamiliaresModelForm(request.POST, prefix='antecedentes_familiares')
        form_aparatos = AparatosModelForm(request.POST, prefix='aparatos')
        form_examen_fisico = ExamenFisicoModelForm(request.POST, prefix='examen_fisico')
        form_planteos = PlanteosModelForm(request.POST, prefix='planteos')
        form_metodologias = MetodologiasModelForm(request.POST, prefix='metodologias')

        if form_historia.is_valid() and form_diagnostico.is_valid():
            # -- asigno el paciente antes de guardar
            form_historia.instance.paciente_id = paciente
            # -- asigno el codigo antes de guardar
            form_historia.instance.codigo = request.POST.get('codigo')

            historia = form_historia.save(commit=False)
            historia.diagnostico = form_diagnostico.save()
            historia.anamnesis = form_anamnesis.save()
            historia.antecedentes_personales = form_antecedentes_personales.save()
            historia.habitos = form_habitos.save()
            historia.antecedentes_familiares = form_antecedentes_familiares.save()
            historia.aparatos = form_aparatos.save()
            historia.examen_fisico = form_examen_fisico.save()
            historia.planteos = form_planteos.save()
            historia.metodologias = form_metodologias.save()
            historia.save()

            msg = 'La historia clinica se creó con éxito'
            # -- si es internacion, ir a agregarle una ubicacion
            if form_historia.instance.tipo == 1:
                messages.success(request, msg + ', ahora asignele una uicación al paciente')
                return redirect('crear_ubicacion', historia=historia.id)
            else:
                messages.success(request, msg)
                return redirect('historias:list')
        else:
            # -- si hay un error, debo agregar en el contexto para mostrar los
            # -- errores en el form y mostrar el respectivo msg
            if form_historia.is_valid() is False:
                messages.error(request, 'Revise el formulario de general.')
                ctx['form_historia'] = form_historia

            if form_diagnostico.is_valid() is False:
                messages.error(request, 'Revise el formulario de diagnóstico.')
                ctx['form_diagnostico'] = form_diagnostico

    return render(request, 'historias/historias_form.html', ctx)