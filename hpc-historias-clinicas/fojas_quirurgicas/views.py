from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin

from .models import FojasQuirurgicas
from ..historias.models import Historias


class FojasQuirurgicasMixin(object):
    def success_msg(self):
        return NotImplemented

    def descarga_msg(self, ic_id):
        return " Click en el siguiente link para Descargar e Imprimir</a>"

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

        return qs
