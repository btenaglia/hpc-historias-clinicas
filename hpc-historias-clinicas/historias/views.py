# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from ..pacientes.models import Pacientes
from .models import Historias, Ubicaciones
from ..diagnosticos.models import Diagnosticos
from ..anamnesis.models import Anamnesis
from ..antecedentes_familiares.models import AntecedentesFamiliares
from ..antecedentes_personales.models import AntecedentesPersonales
from ..aparatos.models import Aparatos
from ..examen_fisico.models import ExamenFisico
from ..habitos.models import Habitos
from ..metodologias.models import Metodologias
from ..planteos.models import Planteos
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


class HistoriasListView(LoginRequiredMixin, ListView):
    """
    Listado de historias clinicas
    """
    model = Historias


class HistoriasPacienteListView(LoginRequiredMixin, ListView):
    """ Ver historias de un paciente determinado """
    model = Historias

    def get_queryset(self):
        return Historias.objects.filter(paciente_id=self.kwargs['paciente']).all()

    def get_context_data(self, **kwargs):
        ctx = super(HistoriasPacienteListView, self).get_context_data(**kwargs)
        ctx['paciente'] = Pacientes.objects.filter(pk=self.kwargs['paciente']).get()
        return ctx


class HistoriasMixin(object):
    """
    Funcionalidad común para las historias
    """
    success_url = '/historias'

    def success_msg(self):
        return NotImplemented

    def get_context_data(self, **kwargs):
        ctx = super(HistoriasMixin, self).get_context_data(**kwargs)
        historia = get_object_or_404(Historias, id=self.kwargs['pk'])
        ctx['historia'] = historia
        ctx['paciente'] = get_object_or_404(Pacientes, id=historia.paciente.id)
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(HistoriasMixin, self).get_success_url()


class UbicacionCreateView(LoginRequiredMixin, HistoriasMixin, CreateView):
    """
    Asignar ubicacion para un determinada historia clínica
    """
    model = Ubicaciones
    fields = ['cama', 'sala']
    success_msg = 'El paciente se ubicó correctamente.'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = None

        if form.is_valid():
            try:
                # -- asigno la historia
                form.instance.historia_id = self.kwargs['pk']
                form.save()
                return self.form_valid(form)
            except IntegrityError:
                messages.error(self.request, 'Error: La historia clínica ya cuenta con una ubicación.')
                return self.form_invalid(**{'form': form})
        else:
            return self.form_invalid(**{'form': form})


class UbicacionUpdateView(LoginRequiredMixin, HistoriasMixin, UpdateView):
    """
    Reubicar un paciente
    """
    model = Ubicaciones
    fields = ['cama', 'sala']
    success_msg = 'El paciente se reubicó correctamente.'

    def get_object(self, queryset=None):
        return Ubicaciones.objects.filter(historia=self.kwargs['pk']).get()


class HistoriaEstadoUpdateView(LoginRequiredMixin, HistoriasMixin, UpdateView):
    """ Modificar el estado de una historia """
    model = Historias
    fields = ['estado']
    template_name = 'historias/historias_estados_form.html'
    success_msg = "Se ha cambiado el estado de la historia."

    def form_valid(self, form):
        # -- liberamos la ubicacion
        if form.instance.estado is not None:
            Ubicaciones.liberar_ubicacion(form.instance.id)
        return super(HistoriaEstadoUpdateView, self).form_valid(form)


@login_required(redirect_field_name='accounts/login/')
def crear_historia(request, paciente):
    """
    Creacion de una historia clinica
    """
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

            msg = 'La historia clinica se creó con éxito.'
            # -- si es internacion, ir a agregarle una ubicacion
            if form_historia.instance.tipo == 1:
                messages.success(request, msg + ', ahora asignele una uicación al paciente.')
                return redirect('historias:ubicacion_create', pk=historia.id)
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


@login_required(redirect_field_name='accounts/login/')
def editar_historia(request, pk):
    """
    Editar datos de una historia clinica
    """
    if pk:
        # -- realizo las consultas para  obtener los datos para
        # -- rellenar los forms
        historia = get_object_or_404(Historias, pk=pk)
        anamnesis_instance = get_object_or_404(Anamnesis, pk=historia.anamnesis_id)
        antecedentes_familiares_instance = get_object_or_404(AntecedentesFamiliares, pk=historia.antecedentes_familiares_id)
        antecedentes_personales_instance = get_object_or_404(AntecedentesPersonales, pk=historia.antecedentes_personales_id)
        aparatos_instance = get_object_or_404(Aparatos, pk=historia.aparatos_id)
        diagnostico_instance = get_object_or_404(Diagnosticos, pk=historia.diagnostico_id)
        examen_fisico_instance = get_object_or_404(ExamenFisico, pk=historia.examen_fisico_id)
        habitos_instance = get_object_or_404(Habitos, pk=historia.habitos_id)
        metodologias_instance = get_object_or_404(Metodologias, pk=historia.metodologias_id)
        planteos_instance = get_object_or_404(Planteos, pk=historia.planteos_id)

        ctx = {
            'paciente': get_object_or_404(Pacientes, id=historia.paciente_id),
            'form_historia': HistoriasModelForm(prefix='historia', instance=historia),
            'form_diagnostico': DiagnosticosModelForm(prefix='diagnostico', instance=diagnostico_instance),
            'form_anamnesis': AnamnesisModelForm(prefix='anamnesis', instance=anamnesis_instance),
            'form_antecedentes_personales': AntecedentesPersonalesModelForm(prefix='antecedentes_personales', instance=antecedentes_personales_instance),
            'form_habitos': HabitosModelForm(prefix='habitos', instance=habitos_instance),
            'form_antecedentes_familiares': AntecedentesFamiliaresModelForm(prefix='antecedentes_familiares', instance=antecedentes_familiares_instance),
            'form_aparatos': AparatosModelForm(prefix='aparatos', instance=aparatos_instance),
            'form_examen_fisico': ExamenFisicoModelForm(prefix='examen_fisico', instance=examen_fisico_instance),
            'form_planteos': PlanteosModelForm(prefix='planteos', instance=planteos_instance),
            'form_metodologias': MetodologiasModelForm(prefix='metodologias', instance=metodologias_instance)
        }

    if request.method == "POST":
        form_historia = HistoriasModelForm(request.POST, prefix='historia', instance=historia)
        form_diagnostico = DiagnosticosModelForm(request.POST, prefix='diagnostico', instance=diagnostico_instance)
        form_anamnesis = AnamnesisModelForm(request.POST, prefix='anamnesis', instance=anamnesis_instance)
        form_antecedentes_personales = AntecedentesPersonalesModelForm(request.POST, prefix='antecedentes_personales',
                                                                       instance=antecedentes_personales_instance)
        form_habitos = HabitosModelForm(request.POST, prefix='habitos', instance=habitos_instance)
        form_antecedentes_familiares = AntecedentesFamiliaresModelForm(request.POST, prefix='antecedentes_familiares',
                                                                       instance=antecedentes_familiares_instance)
        form_aparatos = AparatosModelForm(request.POST, prefix='aparatos', instance=aparatos_instance)
        form_examen_fisico = ExamenFisicoModelForm(request.POST, prefix='examen_fisico',
                                                   instance=examen_fisico_instance)
        form_planteos = PlanteosModelForm(request.POST, prefix='planteos', instance=planteos_instance)
        form_metodologias = MetodologiasModelForm(request.POST, prefix='metodologias', instance=metodologias_instance)

        if form_historia.is_valid() and form_diagnostico.is_valid():
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

            messages.success(request, 'La historia clínica se editó con éxito.')
            return redirect('historias:list')
        else:
            messages.error(request, 'Errores al editar el formulario, por favor revisarlos.')
            ctx['form_historia'] = form_historia
            ctx['form_diagnostico'] = form_diagnostico

    return render(request, 'historias/historias_form.html', ctx)

