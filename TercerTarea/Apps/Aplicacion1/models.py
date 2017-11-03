from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Empleado(models.Model):

    tipo_habitacion = (
    ('SI','SIMPLE'),
    ('DO','DOBLE'),
    )
    tipo = models.CharField(
    max_length=2,
    choices=tipo_habitacion,
    default= 'SI',
    )


    numero_habitacion = (
    ('UN','1'),
    ('DO','2'),
    ('TR','3'),
    ('CU','4'),
    ('CI','5'),
    ('SE','6'),
    ('SI','7'),
    ('OC','8'),
    )
    numero = models.CharField(
    max_length=2,
    choices=numero_habitacion,
    default= 'UN',
    )
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=8)
    salida = models.CharField(max_length=30)
    ingreso = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    nit = models.CharField(max_length=10)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s %s %s %s %s' % (self.nombre, self.apellido, self.tipo, self.numero, self.ingreso)

class Book(models.Model):
    BOOK_CHOICES = (
        ('Habitacion 1','Habitacion 1'),
        ('Habitacion 2','Habitacion 2'),
        ('Habitacion 3','Habitacion 3'),
        ('Habitacion 4','Habitacion 4'),
        ('Habitacion 5','Habitacion 5'),
        ('Habitacion 6','Habitacion 6'),
        ('Habitacion 7','Habitacion 7'),
        ('Habitacion 8','Habitacion 8'),
    )
    title = MultiSelectField(choices = BOOK_CHOICES)
   

class Repara(models.Model): 
    
    total = models.CharField(max_length=10)
    piezas = models.CharField(max_length=500)
    entrega = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.piezas, self.total)

class Login(models.Model): 
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=25)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username


class Consultas(models.Model): 
    
    tipo_habitacion = (
    ('SI','SIMPLE'),
    ('DO','DOBLE'),
    )
    direccion = models.CharField(
    max_length=2,
    choices=tipo_habitacion,
    default= 'SI',
    )
   
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    consulta = models.CharField(max_length=1000)
    fecha = models.CharField(max_length=20)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return '%s %s %s' % (self.nombre, self.telefono, self.consulta)

class Factura(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    detalle = models.ManyToManyField(Empleado)
    cancelar = models.CharField(max_length=20)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.nit, self.detalle)



   