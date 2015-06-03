# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from easy_pdf.views import PDFTemplateView
from ..historias.models import Historias, Ubicaciones
from ..evoluciones.models import Evoluciones
from ..inter_consultas.models import InterConsultas
from ..fojas_quirurgicas.models import FojasQuirurgicas
from ..epicrisis.models import Epicrisis
from ..metodologias.models import Metodologias


class ReporteHistoriaClinica(DetailView):
    """
    Página para poder imprimir todas las historias clínicas
    """
    template_name = 'reportes/historia.html'
    model = Historias
    context_object_name = 'historia'


class ReporteInterConsulta(PDFTemplateView):
    """
    Impresion de una hoja de inter consulta
    """
    template_name = 'reportes/inter_consulta.html'
 
    def get_context_data(self, pk):
        ctx = super(ReporteInterConsulta, self).get_context_data()
        ic = get_object_or_404(InterConsultas, pk=pk)                 
        ctx['historia'] = ic.historia
        ctx['madre'] = True
        ctx['inter_consulta'] = ic
        return ctx
   

class ReporteEvolucion(PDFTemplateView):
    """
    Impresión de una hoja de evolucion
    """
    template_name = "reportes/evolucion.html"
    pdf_filename = None

    def get_context_data(self, pk):
        ctx = super(ReporteEvolucion, self).get_context_data()
        evolucion = get_object_or_404(Evoluciones, pk=pk)
        ctx['historia'] = evolucion.historia
        ctx['madre'] = False
        ctx['evolucion'] = evolucion
        return ctx


class ReporteFojaQuirurgica(PDFTemplateView):
    """
    Impresion de una hoja de Foja Quirurgica
    """
    template_name = 'reportes/foja_quirurgica.html'

    def get_context_data(self, pk):
        ctx = super(ReporteFojaQuirurgica, self).get_context_data()
        foja = get_object_or_404(FojasQuirurgicas, pk=pk)
        ctx['historia'] = foja.historia
        ctx['foja'] = foja
        return ctx


class ReporteEpicrisis(PDFTemplateView):
    """
    Impresion de una hoja de Epicrisis
    """
    template_name = 'reportes/epicrisis.html'

    def get_context_data(self, pk):
        ctx = super(ReporteEpicrisis, self).get_context_data()
        ctx['epicrisis'] = get_object_or_404(Epicrisis, pk=pk)
        return ctx


class ReporteHistoriaClinicaPagina1(PDFTemplateView):
    """
    Impresion de historia clinica
    Pagina 1
    """
    template_name = 'reportes/historia_clinica_page1.html'

    def get_context_data(self, pk):
        ctx = super(ReporteHistoriaClinicaPagina1, self).get_context_data()
        ctx['historia'] = get_object_or_404(Historias, pk=pk)
        return ctx


class ReporteHistoriaClinicaMixin(PDFTemplateView):
    """
    Mixin para imprimir las diferentes hojas
    de las historias clinicas
    """
    def get_context_data(self, **kwargs):
        ctx = super(ReporteHistoriaClinicaMixin, self).get_context_data(**kwargs)
        ctx['historia'] = get_object_or_404(Historias, pk=self.kwargs['pk'])
        ctx['madre'] = True
        return ctx


class ReporteHistoriaClinicaPagina3(ReporteHistoriaClinicaMixin):
    """
    Impresion de historia clinica
    Pagina 3
    """
    template_name = 'reportes/historia_clinica_page3.html'


class ReporteHistoriaClinicaPagina5(ReporteHistoriaClinicaMixin):
    """
    Impresion de historia clinica
    Pagina 5
    """
    template_name = 'reportes/historia_clinica_page5.html'


class ReporteHistoriaClinicaPagina7(ReporteHistoriaClinicaMixin):
    """
    Impresion de historia clinica
    Pagina 7
    """
    template_name = 'reportes/historia_clinica_page7.html'

    def get_context_data(self, **kwargs):
        ctx = super(ReporteHistoriaClinicaPagina7, self).get_context_data(**kwargs)
        ctx['metodologias'] = Metodologias.objects.filter(historia=self.kwargs['pk']).all()
        return ctx


class ReporteHistoriaClinicaPagina4(ReporteHistoriaClinicaMixin):
    """
    Impresion de historia clinica
    Pagina 4
    """
    template_name = 'reportes/historia_clinica_page4.html'


class ReporteHistoriaClinicaPagina6(ReporteHistoriaClinicaMixin):
    """
    Impresion de historia clinica
    Pagina 6
    """
    template_name = 'reportes/historia_clinica_page6.html'


class ReportesInternados(PDFTemplateView):

    template_name = 'reportes/internados.html'

    def get_context_data(self, **kwargs):
        ctx = super(ReportesInternados, self).get_context_data(**kwargs)
        ctx['internados'] = Ubicaciones.objects.order_by('sala').all()
        return ctx



