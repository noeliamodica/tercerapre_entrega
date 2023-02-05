from django import forms

# Create your forms here.

class EstudiantesFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)

class CarrerasFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    duracion = forms.CharField(max_length=10)

class ProfesoresFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)
