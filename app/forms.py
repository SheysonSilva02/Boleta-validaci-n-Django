from django import forms
from .models import Empleado

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'