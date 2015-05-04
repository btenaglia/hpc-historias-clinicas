# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView
from ..historias.models import Historias
from ..evoluciones.models import Evoluciones
from ..inter_consultas.models import InterConsultas
from ..fojas_quirurgicas.models import FojasQuirurgicas


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
