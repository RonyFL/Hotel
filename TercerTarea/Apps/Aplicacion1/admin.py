from django.contrib import admin
from .models import Empleado,Book,Repara,Consultas,Factura

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Book)
admin.site.register(Repara)
admin.site.register(Consultas)
admin.site.register(Factura)
