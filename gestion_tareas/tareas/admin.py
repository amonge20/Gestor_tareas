from django.contrib import admin
from .models import Incidencia

# Register your models here.
@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'cliente', 'categoria', 'prioridad', 'fecha_creacion')
    list_filter = ('categoria', 'prioridad', 'fecha_creacion')
    search_fields = ('asunto', 'descripcion', 'cliente__username')