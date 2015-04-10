from django import template
from ..models import Ubicaciones
register = template.Library()

@register.filter
def tiene_ubicacion(obj, historia_id):
    """
    Devuelve 1 si la historia que se pasa como parametro tienen ubicacion
    """
    return Ubicaciones.objects.filter(historia=historia_id).count()