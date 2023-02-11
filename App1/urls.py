
from django.urls import path
from App1.views import *

urlpatterns = [
    path('', inicio, name= "Inicio"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('carreras/', carrera, name="Carreras"),
    path('profesores/', profesor, name="Profesores"),
    path('carreraFormulario/', carreraFormulario, name="FormularioCarrera"),
    path('buscarCamada/', busquedaCamada , name="BuscarCamada"),
    path('resultados/', resultados , name="Resultados"),
]
 