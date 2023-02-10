from django.shortcuts import render
from App1.models import *
from App1.forms import CarreraFormulario

# Create your views here.

#------------------------------------------
def inicio(request):
      return render(request, "App1/inicio.html")

def estudiante(request):

    todas= Estudiantes.objects.all()
    return  render (request, "App1/estudiantes.html")


 #Para Carreras.

def carrera(request):

    todas= Carreras.objects.all()
    return  render (request, "App1/carreras.html")

def carreraFormulario(request):

      if request.method == "POST":

            formulario1 = CarreraFormulario(request.POST)
            if formulario1.is_valid():
                  info = formulario1.cleaned_data
                  carrera = Carreras(nombre=info['nombre'], camada=info['camada'])
                  carrera.save()
                  return  render (request, "App1/inicio.html")

            else: 
                  formulario1 = CarreraFormulario()

            return  render(request, "App1/carreraFormulario.html", {"form1":formulario1})

#Para Profesores.

def profesor(request):

    todas= Profesores.objects.all()
    return  render (request, "App1/profesores.html")

#Para buscar
