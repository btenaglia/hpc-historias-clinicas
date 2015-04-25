# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from easy_pdf.views import PDFTemplateView
from ..evoluciones.models import Evoluciones
from ..inter_consultas.models import InterConsultas


class ReporteHistoriaClinica(PDFTemplateView):
    template_name = 'reportes/historia.html'


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
        # -- asigno el nombre al archivo pdf
        self.pdf_filename = "inter_consulta_%s.pdf" % ic.historia.codigo
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
        # -- asigno el nombre al archivo pdf
        self.pdf_filename = "evolucion_%s.pdf" % evolucion.historia.codigo
        return ctx
