# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin

from .models import Evoluciones
from ..historias.models import Historias


class EvolucionesMixin(object):

    def success_msg(self):
        return NotImplemented

    def descarga_msg(self , evolucion_id):
        # -- msg para la descar de la evolucion
        return ' Click en el siguiente link para <a target="_blank" href="/reportes/evolucion/%s">Descargar e Imprimir</a>' % str(evolucion_id)

    def get_context_data(self, **kwargs):
        # -- obtengo los datos de la historia clínica
        ctx = super(EvolucionesMixin, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/evoluciones/%s' % (self.kwargs['historia'])


class EvolucionesListView(LoginRequiredMixin, EvolucionesMixin, ListView):
    """Lista de evoluciones"""
    def get_queryset(self):
        # -- traigo todas las evoluciones de una historia determinada
        qs = Evoluciones.objects.filter(historia=self.kwargs['historia'])

        # filtro por fecha ingreso
        fecha = self.request.GET.get('fecha')
        if fecha:
            date = fecha.split('/')
            date = date[2]+'-'+date[1]+'-'+date[0]
            qs = qs.filter(fecha=date)

        # filtro por palabra clave
        palabra_clave = self.request.GET.get('palabra_clave')
        if palabra_clave:
            qs = qs.filter(descripcion__icontains=palabra_clave)

        return qs


class EvolucionesCreateView(LoginRequiredMixin, EvolucionesMixin, CreateView):
    """Crear una nueva evolucion"""
    model = Evoluciones
    fields = ['fecha', 'descripcion']
    success_msg = 'Se agregó una nueva evolución.'

    def get_success_url(self):
        # -- ontengo el id de la reciente evolucion agregada,
        # -- se necesita para armar el link de descarga
        pk = Evoluciones.objects.latest('id').id
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(EvolucionesCreateView, self).get_success_url()

    def post(self, request, *args, **kwargs):
        # -- Es necesario indicarle el Id de la historia
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = None

        form.instance.historia_id = self.kwargs['historia']
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class EvolucionesUpdateView(LoginRequiredMixin, EvolucionesMixin, UpdateView):
    """Modificar una evolucion"""
    model = Evoluciones
    fields = ['fecha', 'descripcion']
    success_msg = 'La evolución se modificó con éxito.'

    def get_success_url(self):
        # -- obtengo id de la evolucion ya que se necesita para armar el link de descarga
        if self.kwargs['pk']:
            self.success_msg += self.descarga_msg(self.kwargs['pk'])

        return super(EvolucionesUpdateView, self).get_success_url()


class EvolucionesDeleteView(LoginRequiredMixin, EvolucionesMixin, DeleteView):
    """Eliminar evolucion"""
    model = Evoluciones
    success_msg = 'La evolución se eliminó con éxito.'
