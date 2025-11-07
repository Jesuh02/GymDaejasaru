from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Entrenadores
    path('entrenadores/', views.EntrenadorListView.as_view(), name='entrenador_list'),
    path('entrenadores/crear/', views.entrenador_create, name='entrenador_create'),
    path('entrenadores/editar/<int:pk>/', views.entrenador_update, name='entrenador_update'),
    path('entrenadores/eliminar/<int:pk>/', views.entrenador_delete, name='entrenador_delete'),
    
    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    
    # Clases
    path('clases/', views.ClaseListView.as_view(), name='clase_list'),
    path('clases/crear/', views.clase_create, name='clase_create'),
    path('clases/editar/<int:pk>/', views.clase_update, name='clase_update'),
    path('clases/eliminar/<int:pk>/', views.clase_delete, name='clase_delete'),
    
    # Asistencias
    path('asistencias/', views.AsistenciaClaseListView.as_view(), name='asistencia_list'),
    path('asistencias/crear/', views.asistencia_create, name='asistencia_create'),
    path('asistencias/eliminar/<int:pk>/', views.asistencia_delete, name='asistencia_delete'),
    
    # Membresías
    path('membresias/', views.ClienteMembresiaListView.as_view(), name='membresia_list'),
    path('membresias/crear/', views.membresia_create, name='membresia_create'),
    path('membresias/editar/<int:pk>/', views.membresia_update, name='membresia_update'),
    path('membresias/eliminar/<int:pk>/', views.membresia_delete, name='membresia_delete'),
    
    # Especialidades
    path('especialidades/', views.EspecialidadEntrenadorListView.as_view(), name='especialidad_list'),
    path('especialidades/crear/', views.especialidad_create, name='especialidad_create'),
    path('especialidades/eliminar/<int:pk>/', views.especialidad_delete, name='especialidad_delete'),
]

