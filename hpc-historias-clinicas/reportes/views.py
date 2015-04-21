# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from easy_pdf.views import PDFTemplateView
from ..evoluciones.models import Evoluciones

class ReporteEvolucion(PDFTemplateView):
    """
    Impresión de una hoja de evolucion
    """
    template_name = "reportes/evolucion.html"

    def get_context_data(self, pk):
        ctx = super(ReporteEvolucion, self).get_context_data()
        ctx['evolucion'] = get_object_or_404(Evoluciones, pk=pk)
        return ctx
