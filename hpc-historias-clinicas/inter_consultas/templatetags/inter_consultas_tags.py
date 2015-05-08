from django import template
from ..models import InterConsultas
register = template.Library()

@register.simple_tag
def total_inter_consultas(historia_id):
	"""
	Devuelve el total de inter consultas para una historia clinica
	"""
	return InterConsultas.objects.filter(historia=historia_id).count()