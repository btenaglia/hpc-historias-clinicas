from django import forms
from .models import Epicrisis


class EpicrisisForm(forms.ModelForm):
    class Meta:
        model = Epicrisis
        exclude = ('historia', )
