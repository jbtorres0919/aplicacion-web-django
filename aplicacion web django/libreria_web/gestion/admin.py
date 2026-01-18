from django.contrib import admin
from .models import Libreria, Empleado, Libro

admin.site.register(Libreria)
admin.site.register(Empleado)
admin.site.register(Libro)