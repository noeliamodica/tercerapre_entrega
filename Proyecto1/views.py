from django.http import HttpResponse
from django.template import Template, Context

def saludo (request,) : 
    return HttpResponse ("Hola Mundo")


def mi_pagina (request) : 

    miHtml=open("C:/Users/noeli/Documents/Programacion/Python/PythonProyecto1/Proyecto1/Proyecto1/plantillas/prueba.html")

    plantilla= Template(miHtml.read())

    miHtml.close()

    miContexto= Context()

    documento= plantilla.render(miContexto)

    return HttpResponse(documento)

    