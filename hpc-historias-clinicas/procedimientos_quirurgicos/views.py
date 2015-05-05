# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from braces.views import LoginRequiredMixin
from .models import ProcedimientosQuirurgicos


class ProcedimientosQuirurgicosMixin(object):

    def success_msg(self):
        return NotImplemented

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return super(ProcedimientosQuirurgicosMixin, self).get_success_url()


class ProcedimientosQuirurgicosListView(LoginRequiredMixin, ListView):
    """ Listado de procedimientos quirurgicos """
    model = ProcedimientosQuirurgicos


class ProcedimientosQuirurgicosCreateView(LoginRequiredMixin, ProcedimientosQuirurgicosMixin, CreateView):
    """ Agregar un nuevo procedimiento quirurgico """
    model = ProcedimientosQuirurgicos
    success_msg = 'El procedimiento quirurgico se creó correctamente.'


class ProcedimientosQuirurgicosUpdateView(LoginRequiredMixin, ProcedimientosQuirurgicosMixin, UpdateView):
    """ Edicion de procedimiento quirurgico """
    model = ProcedimientosQuirurgicos
    success_msg = 'El procedimiento quirurgico fué editado correctamente.'


class ProcedimientosQuirurgicosDeleteView(LoginRequiredMixin, ProcedimientosQuirurgicosMixin, DeleteView):
    """ Eliminar un procedimiento quirurgico """
    model = ProcedimientosQuirurgicos
    success_msg = 'El procedimiento quirurgico fué eliminado correctamente.'
    success_url = '/procedimientos/quirurgicos'


def traer_descripcion(request):
    """ Recupero la descripcion de un procedimiento """
    descripcion = ProcedimientosQuirurgicos.objects.filter(id=request.GET['pk'])
    data = serializers.serialize('json', descripcion, fields={'descripcion'})
    return HttpResponse(data, content_type='application/json')
