from django.forms import ModelForm
from django import forms

from .models import Historias
from ..diagnosticos.models import Diagnosticos
from ..anamnesis.models import Anamnesis
from ..antecedentes_personales.models import AntecedentesPersonales
from ..habitos.models import Habitos
from ..antecedentes_familiares.models import AntecedentesFamiliares
from ..aparatos.models import Aparatos
from ..examen_fisico.models import ExamenFisico
from ..planteos.models import Planteos
from ..metodologias.models import Metodologias, TipoMetodologias


class HistoriasModelForm(ModelForm):
    class Meta:
        model = Historias
        fields = ['tipo', 'fecha_ingreso', 'hora_ingreso', 'medico', 'dpto_cirugia']


class DiagnosticosModelForm(ModelForm):
    class Meta:
        model = Diagnosticos


class AnamnesisModelForm(ModelForm):
    class Meta:
        model = Anamnesis


class AntecedentesPersonalesModelForm(ModelForm):
    class Meta:
        model = AntecedentesPersonales


class HabitosModelForm(ModelForm):
    class Meta:
        model = Habitos


class AntecedentesFamiliaresModelForm(ModelForm):
    class Meta:
        model = AntecedentesFamiliares


class AparatosModelForm(ModelForm):
    class Meta:
        model = Aparatos


class ExamenFisicoModelForm(ModelForm):
    class Meta:
        model = ExamenFisico


class PlanteosModelForm(ModelForm):
    class Meta:
        model = Planteos


class MetodologiasModelForm(forms.Form):
    def __init__(self,  *args, **kwargs):
        super(MetodologiasModelForm, self).__init__( *args, **kwargs)
        tipos_metodologias = TipoMetodologias.objects.values_list('id', 'nombre').all()
        # for tipo in tipos_metodologias:
        #     self.fields['tipo_metodologia_'+str(tipo.id)] = forms.BooleanField()

        self.fields['tipo_metodologias']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=tipos_metodologias, label="Notify and subscribe users to this post:")


