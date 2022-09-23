from django.shortcuts import render
from contextvars import Context
from django.http import HttpResponse, request
from datetime import datetime
from django.template import Template, Context
from AppCoder.views import *
from AppCoder.models import *
from AppCoder.templates import *


# Create your views here.

def inicio(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/inicio.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def vista_datos(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/vista_datos.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def respuesta_datos(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/respuesta_datos.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def template_5(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/form1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def template_6(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/form2.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def template_7(self):
    miHtml = open("C:/Users/carlo/OneDrive/Desktop/Django/P_final_1/proyectofinal/AppCoder/templates/AppCoder/form3.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def formulario_1(request):

    if request.method=="POST":
        
        basico = basicos(Importe_asociado=request.POST["Importe_asociado"],Importe_gastado=request.POST["Importe_gastado"],Fecha_importe=request.POST["Fecha_importe"])

        basico.save()

        return render(request, "AppCoder/form1.html")

    return render(request, "AppCoder/form1.html")

def formulario_2(request):

    if request.method=="POST":
        
        ocio_ = ocio(Importe_asociado=request.POST["Importe_asociado"],Importe_gastado=request.POST["Importe_gastado"],Fecha_importe=request.POST["Fecha_importe"])

        ocio_.save()

        return render(request, "AppCoder/form2.html")

    return render(request, "AppCoder/form2.html")

def formulario_3(request):

    if request.method=="POST":
        
        varios_ = varios(Importe_asociado=request.POST["Importe_asociado"],Importe_gastado=request.POST["Importe_gastado"],Fecha_importe=request.POST["Fecha_importe"])

        varios_.save()

        return render(request, "AppCoder/form3.html")

    return render(request, "AppCoder/form3.html")


def buscador_categoria(request):

    if request.GET["Categoria"] == "ocio":
        modeloResultados = ocio.objects.all()

    if request.GET["Categoria"] == "varios":
        modeloResultados = varios.objects.all()

    if request.GET["Categoria"] == "basico":
        modeloResultados = basicos.objects.all()

    return render(request,'AppCoder/respuesta_datos.html', {"modelo":modeloResultados, "Categoria":request.GET["Categoria"]})

