from django import template
from ..models import Evoluciones

register = template.Library()

@register.simple_tag
def total_evoluciones(historia_id):
    """
    Devuelve el total de evoluciones para una historia clinica
    """
    return Evoluciones.objects.filter(historia=historia_id).count()
