from django.shortcuts import render
from App1.models import *
from App1.forms import *

# Create your views here.

def ver_estudiantes(request):

    todas= Estudiantes.objects.all()
    return  render (request, "AppEstudiantes/estudiantes.html", {"todas": todas})

 
def agregar_estudiantes(request):
 
      if request.method == "POST":
 
            miFormulario = EstudiantesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiantes(nombre=informacion["nombre"], carrera=informacion["carrera"])
                  estudiante.save()
                  return render(request, "AppEstudiantes/estudiantes.html")
      else:
            miFormulario = EstudiantesFormulario()
 
      return render(request, "AppEstudiantes/estudiantesFormulario.html", {"miFormulario": miFormulario})

def buscar_estudiantes(request):
     return  render (request, "AppEstudiantes/buscarEstudiantes.html")

def resultadosEstudiantes(request):
    nombreBusqueda = request.GET ["nombre"]
    resultadosEstudiantes = Estudiantes.objects.filter(nombre_icontains=nombreBusqueda)
    return  render (request, "AppEstudiantes/resultadosEstudiantes.html", {"info1":nombreBusqueda, "info2":resultadosEstudiantes})

 #Para Carreras.

def ver_carreras(request):

    todas= Carreras.objects.all()
    return  render (request, "AppEstudiantes/carreras.html", {"todas": todas})

 
def agregar_carreras(request):
 
      if request.method == "POST":
 
            miFormulario = CarrerasFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  carrera = Carreras(nombre=informacion["nombre"], duracion=informacion["duracion"])
                  carrera.save()
                  return render(request, "AppEstudiantes/carreras.html")
      else:
            miFormulario = CarrerasFormulario()
 
      return render(request, "AppEstudiantes/carrerasFormulario.html", {"miFormulario": miFormulario})

def buscar_carreras(request):
     return  render (request, "AppEstudiantes/buscarCarreras.html")

def resultadosCarreras(request):
    nombreBusqueda = request.GET ["nombre"]
    resultadosCarreras = Carreras.objects.filter(nombre_icontains=nombreBusqueda)
    return  render (request, "AppEstudiantes/resultadosCarreras.html", {"info3":nombreBusqueda, "info4":resultadosCarreras})

#Para Profesores.

def ver_profesores(request):

    todas= Profesores.objects.all()
    return  render (request, "AppEstudiantes/profesores.html", {"todas": todas})

 
def agregar_profesores(request):
 
      if request.method == "POST":
 
            miFormulario = ProfesoresFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  profesor = Profesores(nombre=informacion["nombre"], carrera=informacion["carrera"])
                  profesor.save()
                  return render(request, "AppEstudiantes/profesores.html")
      else:
            miFormulario = ProfesoresFormulario()
 
      return render(request, "AppEstudiantes/profesoresFormulario.html", {"miFormulario": miFormulario})

def buscar_profesores(request):
     return  render (request, "AppEstudiantes/buscarProfesores.html")

def resultadosProfesores(request):
    nombreBusqueda = request.GET ["nombre"]
    resultadosProfesores = Profesores.objects.filter(nombre_icontains=nombreBusqueda)
    return  render (request, "AppEstudiantes/resultadosProfesores.html", {"info5":nombreBusqueda, "info6":resultadosProfesores})
