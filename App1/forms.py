from django import forms

# Create your forms here.

class EstudianteFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)

class CarreraFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()

class ProfesorFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    carrera = forms.CharField(max_length=30)
