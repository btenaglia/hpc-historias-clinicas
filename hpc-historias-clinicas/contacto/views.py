# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..settings import EMAIL_TO
from .forms import ContactoForm


def enviar_contacto(request):
    """
    Enviar email con el formulario de contacto
    a soporte tecnico
    """
    formulario = ContactoForm()

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            mail = EmailMessage(subject='HPC Contacto',
                                from_email=formulario.cleaned_data['email'],
                                to=EMAIL_TO)
            mail.body = 'El usuario %s ha comentado: %s' \
                        % (formulario.cleaned_data['nombre'], formulario.cleaned_data['mensaje'])
            mail.send()
            messages.success(request, "El personal de soporte técnico ha recibido su consulta, "
                                      "pronto nos pondremos en contacto.")
            return HttpResponseRedirect('/')

    ctx = {'form': formulario}
    return render_to_response('contacto/enviar_contacto.html', ctx, context_instance=RequestContext(request))
