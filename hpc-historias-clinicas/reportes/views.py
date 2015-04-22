# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from easy_pdf.views import PDFTemplateView
from ..evoluciones.models import Evoluciones


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
