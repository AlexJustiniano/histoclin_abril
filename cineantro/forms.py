from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


from .models import Paciente, Institucion, Examen

class PacienteModForm(forms.ModelForm):

        class Meta:
            model = Paciente
            fields = '__all__'
            #fields = (
            #	'nombre', 'apellidos', 'institucion', 'f_nac', 'sexo', 'domicilio', 'tel',
            #	'ci', 'seguro', 'procedencia', 'ocupacion', 'ec', 'enfermedad', 'sintomas',
            #	'signos', 'sindromes', 'a_personales', 'a_patologicos', 'a_nopatologicos',
            #	'a_hereditarios', 'a_presuntivo', 'd_definitivo', 'interconsulta'
           #)

class InstitucionModForm(forms.ModelForm):

		class Meta:
			model = Institucion
			fields = '__all__'


class ExamenModForm(forms.ModelForm):

        class Meta:
            model = Examen
            fields = '__all__'

ExamenFormset = forms.modelformset_factory(Examen, form=ExamenModForm, can_delete=True)
