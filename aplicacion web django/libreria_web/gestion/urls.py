from django.urls import path
from . import views

urlpatterns = [
    path('librerias/', views.listar_librerias, name='listar_librerias'),
    path('librerias/nueva/', views.crear_libreria, name='crear_libreria'),
    path('librerias/editar/<int:id>/', views.editar_libreria, name='editar_libreria'),

    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/nuevo/', views.crear_empleado, name='crear_empleado'),

    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/nuevo/', views.crear_libro, name='crear_libro'),
]
