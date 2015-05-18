# -*- coding: utf-8 -*-
from django import forms


class ContactoForm(forms.Form):
    """
    Formulario para el contacto con
    soporte técnico
    """
    nombre = forms.CharField(widget=forms.TextInput, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(widget=forms.TextInput, required=False, label='Teléfono')
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
