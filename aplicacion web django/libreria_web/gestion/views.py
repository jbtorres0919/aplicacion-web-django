from django.shortcuts import render, redirect
from .models import Libreria, Empleado, Libro
from .forms import LibreriaForm, EmpleadoForm, LibroForm

def listar_librerias(request):
    librerias = Libreria.objects.all()
    return render(request, 'libreria/listar.html', {'librerias': librerias})

def crear_libreria(request):
    form = LibreriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_librerias')
    return render(request, 'libreria/form.html', {'form': form})

def editar_libreria(request, id):
    libreria = Libreria.objects.get(id=id)
    form = LibreriaForm(request.POST or None, instance=libreria)
    if form.is_valid():
        form.save()
        return redirect('listar_librerias')
    return render(request, 'libreria/form.html', {'form': form})

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/listar.html', {'empleados': empleados})

def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_empleados')
    return render(request, 'empleado/form.html', {'form': form})

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libro/listar.html', {'libros': libros})

def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_libros')
    return render(request, 'libro/form.html', {'form': form})
