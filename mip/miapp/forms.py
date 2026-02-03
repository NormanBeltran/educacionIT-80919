from django import forms

class FormularioCurso(forms.Form):
    nombre = forms.CharField(max_length=50, help_text="Ingrese nombre del curso")
    inscriptos = forms.IntegerField()
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