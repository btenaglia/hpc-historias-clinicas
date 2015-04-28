# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from braces.views import LoginRequiredMixin
from .models import MotivosConsultas


class MotivosMixin(object):

    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(MotivosMixin, self).get_success_url()


class MotivosListView(LoginRequiredMixin, ListView):
    """ Listado de motivo de consulta """
    model = MotivosConsultas


class MotivosCreateView(LoginRequiredMixin, MotivosMixin, CreateView):
    """ Agregar un nuevo motivo de consulta """
    model = MotivosConsultas
    success_msg = 'El motivo de consulta se creó correctamente.'


class MotivosUpdateView(LoginRequiredMixin, MotivosMixin, UpdateView):
    """ Edicion de motivo de consulta """
    model = MotivosConsultas
    success_msg = 'El motivo de consulta fué editado.'


class MotivosDeleteView(LoginRequiredMixin, MotivosMixin, DeleteView):
    """ Eliminar un motivo de consulta """
    model = MotivosConsultas
    success_msg = 'El motivo de consulta fué eliminado.'
    success_url = '/motivos'


def traer_enfermedad(request):
    print 'hello'
    tipo_motivos = MotivosConsultas.objects.filter(id=request.GET['pk'])
    data = serializers.serialize('json', tipo_motivos, fields={'descripcion'})
    return HttpResponse(data, content_type='application/json')
