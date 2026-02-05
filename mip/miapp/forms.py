from django import forms
from django.forms import ModelForm
from .models import *

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos") 


"""
    profesor = forms.CharField(max_length=50)
    solo_empresas = forms.BooleanField(label="Es para empresas?", required=False)
    TURNOS = (
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )
    turno = forms.ChoiceField(choices=TURNOS, required=True)
    fecha_inicio = forms.DateField(input_formats=["%d/%m/%Y"])
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=False)

"""        