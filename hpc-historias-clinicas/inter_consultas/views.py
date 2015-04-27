# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import InterConsultas
from ..historias.models import Historias


class InterConsultasMixin(object):

    def success_msg(self):
        return NotImplemented

    def descarga_msg(self, ic_id):
        return " Click en el siguiente link para <a href='/reportes/inter/consultas/%s'>Descargar e Imprimir</a>" % str(ic_id)

    def get_context_data(self, **kwargs):
        """Es necesario traer los datos de la historia clinica"""
        ctx = super(InterConsultasMixin, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/inter/consultas/%s' % (self.kwargs['historia'])


class InterConsultasListView(LoginRequiredMixin, InterConsultasMixin, ListView):
    """
    Obtengo las inter-consultas de una historia clinica
    """
    def get_queryset(self):
        qs = InterConsultas.objects.filter(historia=self.kwargs['historia'])

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


class InterConsultasCreateView(LoginRequiredMixin, InterConsultasMixin, CreateView):
    """ Creacion de una inter consulta """
    model = InterConsultas
    fields = ['fecha', 'descripcion']
    success_msg = 'La inter consulta se agregó con éxito.'

    def get_success_url(self):
        # -- armo el msg para la descarga de la inter consulta
        # -- obtengo el ultimo id ingresado, es necesario para
        # -- armar la ulr de descarga
        pk = InterConsultas.objects.latest('id').id
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(InterConsultasCreateView, self).get_success_url()

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


class InterConsultasUpdateView(LoginRequiredMixin, InterConsultasMixin, UpdateView):
    """ Edicion de una inter consulta """
    model = InterConsultas
    fields = ['fecha', 'descripcion']
    success_msg = 'La inter consulta se editó con éxito.'

    def get_success_url(self):
        # -- armo el msg para la descarga de la inter consulta
        # -- obtengo el ultimo id ingresado, es necesario para
        # -- armar la ulr de descarga
        pk = self.kwargs['pk']
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(InterConsultasUpdateView, self).get_success_url()


class InterConsultasDeleteView(LoginRequiredMixin, InterConsultasMixin, DeleteView):
    """ Eliminar una inter consulta """
    model = InterConsultas
    success_msg = 'La inter consulta se eliminó con éxito.'
