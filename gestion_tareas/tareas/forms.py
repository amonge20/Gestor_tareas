from django import forms
from .models import Tarea, Incidencia

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'prioridad', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['asunto', 'descripcion', 'categoria', 'archivo']      
        