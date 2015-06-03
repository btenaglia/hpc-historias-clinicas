from django import template
from ..models import FojasQuirurgicas

register = template.Library()

@register.simple_tag
def total_fojas_quirurgicas(historia_id):
    """
    Devuelve el total de fojas quirurgicas para una historia clinica
    """
    return FojasQuirurgicas.objects.filter(historia=historia_id).count()


@register.assignment_tag
def obtener_fojas_quirurgicas(historia_id):
    """
    Obtener ls fojas quirurgicas de una determinada historia clinica
    """
    return FojasQuirurgicas.objects.filter(historia=historia_id).all()