from django.db import models

    # Create your models here.

    #class curso(models.Model):
    #    nombre = models.CharField(max_length=60)
    #    camada = models.CharField(max_length=30)
    # class estudiante(models.Model):
    #    nombre = models.CharField(max_length=60)
    #    apellido = models.CharField(max_length=60)
    #    correo = models.EmailField()
    #class profesor(models.Model):
    # #   nombre = models.CharField(max_length=60)
    #    apellido = models.CharField(max_length=60)
    #    profesion = models.CharField(max_length=60)
    #   correo = models.EmailField()
    #class entregable(models.Model):
    #    nombre = models.CharField(max_length=60)
    #    fecha_entrega = models.DateField()

class basicos(models.Model):
    Importe_asociado = models.CharField(max_length=60)
    Importe_gastado = models.IntegerField()
    Fecha_importe = models.DateField()

class ocio(models.Model):
    Importe_asociado = models.CharField(max_length=60)
    Importe_gastado = models.IntegerField()
    Fecha_importe = models.DateField()

class varios(models.Model):
    Importe_asociado = models.CharField(max_length=60)
    Importe_gastado = models.IntegerField()
    Fecha_importe = models.DateField()
