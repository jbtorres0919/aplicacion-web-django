from django import forms
from .models import Libreria, Empleado, Libro

class LibreriaForm(forms.ModelForm):
    class Meta:
        model = Libreria
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
