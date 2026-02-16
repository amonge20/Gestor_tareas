from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    prioridad_choices = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prioridad = models.CharField(max_length=10, choices=prioridad_choices, default='media')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.titulo
    
# Clase para que los clientes envien incidencias
class Incidencia(models.Model):
    CATEGORIAS = [
        ('tecnico', 'Soporte Técnico'),
        ('facturacion', 'Facturación'),
        ('acceso', 'Problema de acceso'),
    ]

    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En proceso'),
        ('cerrada', 'Cerrada'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='tecnico')
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='media')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    archivo = models.FileField(upload_to='incidencias/', null=True, blank=True)  # <--- NUEVO

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} - {self.cliente.username}"