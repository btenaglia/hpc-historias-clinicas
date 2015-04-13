# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin
from .models import TipoDiagnosticos


class TipoDiagnosticosMixin(object):

    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(TipoDiagnosticosMixin, self).get_success_url()


class TipoDiagnosticosListView(LoginRequiredMixin, ListView):
    """ Listado de diagnosticos """
    model = TipoDiagnosticos


class TipoDiagnosticosCreateView(LoginRequiredMixin, TipoDiagnosticosMixin, CreateView):
    """ Agregar un nuevo diagnostico """
    model = TipoDiagnosticos
    success_msg = 'El diagnostico se creó correctamente.'


class TipoDiagnosticosUpdateView(LoginRequiredMixin, TipoDiagnosticosMixin, UpdateView):
    """ Edicion de diagnostico """
    model = TipoDiagnosticos
    success_msg = 'El diagnostico fué editado.'


class TipoDiagnosticosDeleteView(LoginRequiredMixin, TipoDiagnosticosMixin, DeleteView):
    """ Eliminar un diagnostico """
    model = TipoDiagnosticos
    success_msg = 'El diagnostico fué eliminado.'
    success_url = '/diagnosticos'
