from datetime import datetime
from django import template
from ..models import Ubicaciones
register = template.Library()

@register.filter
def tiene_ubicacion(obj, historia_id):
    """
    Devuelve 1 si la historia que se pasa como parametro tienen ubicacion
    """
    return Ubicaciones.objects.filter(historia=historia_id).count()

@register.assignment_tag
def obtener_ubicacion(historia_id):
    """
    Obtener la sala y la cama de la historia clinica
    """
    return Ubicaciones.objects.values('cama', 'sala', 'comentario').filter(historia=historia_id)[:1]

@register.filter
def calcular_diferencia_dias(fin_dia):
    """
    Obtiene la diferencia de dias entre una fecha y hoy
    """
    hoy = datetime.now()
    end = datetime.strptime(str(fin_dia), '%Y-%m-%d')
    return abs(end - hoy).days