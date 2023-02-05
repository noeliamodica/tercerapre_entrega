
from django.urls import path
from App1.views import *

urlpatterns = [
    path('estudiantes/', ver_estudiantes),
    path('nuevoestudiante/', agregar_estudiantes),
    path('buscarestudiante/', buscar_estudiantes),
    path('resultadosestudiantes/', resultadosEstudiantes),
    path('carreras/', ver_carreras),
    path('nuevacarrera/', agregar_carreras),
    path('buscarcarrera/', buscar_carreras),
    path('resultadoscarreras/', resultadosCarreras),
     path('profesores/', ver_profesores),
    path('nuevoprofesor/', agregar_profesores),
    path('buscarprofesor/', buscar_profesores),
    path('resultadosprofesores/', resultadosProfesores),




]
 