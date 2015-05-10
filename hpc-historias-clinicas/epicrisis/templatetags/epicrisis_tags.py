from django import template
from ..models import Epicrisis

register = template.Library()

@register.assignment_tag
def tiene_epicrisis(historia_id):
    """
    Devuelve datos si existe epicrisis para
    una determinada historia clinica
    """
    return Epicrisis.objects.filter(historia=historia_id).all()
