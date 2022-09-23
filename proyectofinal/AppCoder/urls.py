from django.urls import path
from proyectofinal.views import *
from AppCoder.views import *
from proyectofinal.settings import *

urlpatterns = [

    path('', inicio, name="inicio"),
    path('form1/', formulario_1, name="form1"),
    path('form2/', formulario_2, name="form2"),
    path('form3/', formulario_3, name="form3"),
    path("buscador/", vista_datos, name="buscar"),
    path("respuesta/", buscador_categoria, name="respuesta"),
    ]