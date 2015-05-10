# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from braces.views import LoginRequiredMixin
from .models import Epicrisis
from .forms import EpicrisisForm
from ..historias.models import Historias


class EpicrisisMixin(object):

    def success_msg(self):
        return NotImplemented

    def descarga_msg(self, epicrisis_id):
        # -- msg para la descar la epicrisis
        return ' Click en el siguiente link para <a target="_blank" href="/reportes/evolucion/%s">Descargar e Imprimir</a>' % str(epicrisis_id)

    def get_context_data(self, **kwargs):
        # -- obtengo los datos de la historia clínica
        ctx = super(EpicrisisMixin, self).get_context_data(**kwargs)
        ctx['historia'] = Historias.objects.filter(id=self.kwargs['historia']).get()
        return ctx

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return '/historias'


class EpicrisisCreateView(LoginRequiredMixin, EpicrisisMixin, CreateView):
    """
    Alta de una epicrisis
    """
    template_name = 'epicrisis/epicrisis_form.html'
    form_class = EpicrisisForm
    success_msg = 'La epicrisis se creó con éxito.'

    def get_initial(self):
        """
        Prefill de campos en el formulario.
        Los datos vienen de la historia clinica
        """
        ctx = super(EpicrisisCreateView, self).get_context_data()
        historia = ctx['historia']

        return {
            'antecedentes': 'Internaciones previas: ' + historia.antecedentes_personales.internaciones_previas + '\n'
                            'Antecedentes traumaticos: ' + historia.antecedentes_personales.antecedentes_traumaticos + '\n'
                            'Antecedentes quirurgicos:' + historia.antecedentes_personales.antecedentes_quirurgicos,
            'fecha_egreso': historia.modificado
        }

    def get_success_url(self):
        # -- ontengo el id de la reciente epicrisis agregada,
        # -- se necesita para armar el link de descarga
        pk = Epicrisis.objects.latest('id').id
        if pk:
            self.success_msg += self.descarga_msg(pk)

        return super(EpicrisisCreateView, self).get_success_url()

    def post(self, request, *args, **kwargs):
        # -- le indico el ID de la historia clínica
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        form.instance.historia_id = self.kwargs['historia']
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{'form': form})


class EpicrisisUpdateView(LoginRequiredMixin, EpicrisisMixin, UpdateView):
    """
    Edicion de una epicrisis
    """
    template_name = 'epicrisis/epicrisis_form.html'
    form_class = EpicrisisForm
    model = Epicrisis
    success_msg = 'La epicrisis se editó con éxito.'

