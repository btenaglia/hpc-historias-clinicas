# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import FojasQuirurgicas
from ..medicos.models import Medicos
from ..historias.models import Historias


class FojasQuirurgicasMixin(object):
    def success_msg(self):
        return NotImplemented

    def descarga_msg(self, foja_id):
        return " Click en el siguiente link para <a target='_blank' href='/reportes/foja/quirurgica/%s'>Descargar e Imprimir</a>" % str(foja_id)

    def get_context_data(self, **kwargs):
        """Es necesario traer los datos de la historia clinica"""
        ctx = super(FojasQuirurgicasMixin, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/fojas/quirurgicas/%s' % (self.kwargs['historia'])


class FojasQuirurgicasListView(LoginRequiredMixin, FojasQuirurgicasMixin, ListView):
    """Listado de fojas quirurgicas de las historias"""
    def get_queryset(self):
        qs = FojasQuirurgicas.objects.filter(historia=self.kwargs['historia'])

        # filtro por fecha
        fecha = self.request.GET.get('fecha')
        if fecha:
            date = fecha.split('/')
            date = date[2]+'-'+date[1]+'-'+date[0]
            qs = qs.filter(fecha=date)

        # filtro por cirujano
        cirujano = self.request.GET.get('cirujano')
        if cirujano:
            qs = qs.filter(cirujano=cirujano)

        # palabra clave en procedimiento
        palabra = self.request.GET.get('palabra')
        if palabra:
            qs = qs.filter(procedimiento_quirurgico__icontains=palabra)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super(FojasQuirurgicasListView, self).get_context_data(**kwargs)
        ctx['cirujanos'] = Medicos.objects.all()
        return ctx


class FojasQuirurgicasCreateView(LoginRequiredMixin, FojasQuirurgicasMixin, CreateView):
    """Nueva foja quirurgica"""
    model = FojasQuirurgicas
    fields = ['cirujano', 'ayudante_1', 'ayudante_2', 'ayudante_3', 'fecha',
              'hora_comienzo', 'hora_fin', 'procedimiento_quirurgico', 'descripcion']
    success_msg = 'La foja quirurgica se agregó con éxito.'

    def post(self, request, *args, **kwargs):
        # -- hay que ndicarle el Id de la historia
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = None

        form.instance.historia_id = self.kwargs['historia']
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})

    def get_success_url(self):
        # necesitamos el ultimo id para
        # armar el link de descarga
        pk = FojasQuirurgicas.objects.latest('id').id
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(FojasQuirurgicasCreateView, self).get_success_url()


class FojasQuirurgicasUpdateView(LoginRequiredMixin, FojasQuirurgicasMixin, UpdateView):
    """ Edicion de una foja quirurgica """
    model = FojasQuirurgicas
    fields = ['cirujano', 'ayudante_1', 'ayudante_2', 'ayudante_3', 'fecha',
              'hora_comienzo', 'hora_fin', 'procedimiento_quirurgico', 'descripcion']
    success_msg = 'La foja quirurgica se editó con éxito.'  

    def get_success_url(self):
        pk = self.kwargs['pk']
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(FojasQuirurgicasUpdateView, self).get_success_url() 


class FojasQuirurgicasDeleteView(LoginRequiredMixin, FojasQuirurgicasMixin, DeleteView):
    """ Eliminar una foja quirurgica """
    model = FojasQuirurgicas
    success_msg = 'La foja quirurgica se eliminó con éxito.'          