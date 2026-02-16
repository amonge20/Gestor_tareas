from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('nueva-incidencia/', views.crear_incidencia, name='crear_incidencia'),
    path('incidencia-enviada/', views.incidencia_enviada, name='incidencia_enviada'),
    path('editar-incidencia/<int:pk>/', views.editar_incidencia, name='editar_incidencia'),
    path('eliminar-incidencia/<int:pk>/', views.eliminar_incidencia, name='eliminar_incidencia'),
    path('asignar-incidencia/<int:pk>/', views.asignar_incidencia, name='asignar_incidencia'),
    path('inicio-de-sesion/',views.iniciar_sesion, name="iniciar_sesion"),
]