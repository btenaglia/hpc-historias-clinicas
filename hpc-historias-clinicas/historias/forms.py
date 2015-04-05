from django.forms import ModelForm

from ..diagnosticos.models import Diagnosticos


class DiagnosticosModelForm(ModelForm):
    class Meta:
        model = Diagnosticos

