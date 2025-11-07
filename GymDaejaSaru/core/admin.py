from django.contrib import admin
from .models import *


@admin.register(DatosMaestros)
class DatosMaestrosAdmin(admin.ModelAdmin):
    list_display = ('dama_id', 'dama_nombre', 'dama_valor', 'dama_padre_id', 'dama_estado')
    list_filter = ('dama_estado', 'dama_padre_id')
    search_fields = ('dama_nombre', 'dama_valor')
    list_editable = ('dama_estado',)
    ordering = ('dama_id',)


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('entr_id', 'entr_nombre', 'entr_telefono', 'entr_numero_documento', 'dama_tipo_documento')
    list_filter = ('dama_tipo_documento',)
    search_fields = ('entr_nombre', 'entr_numero_documento', 'entr_telefono')
    ordering = ('entr_nombre',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('clie_id', 'clie_nombre', 'clie_telefono', 'clie_numero_documento', 'dama_tipo_documento')
    list_filter = ('dama_tipo_documento',)
    search_fields = ('clie_nombre', 'clie_numero_documento', 'clie_telefono')
    ordering = ('clie_nombre',)


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('clas_id', 'clas_nombre', 'clas_fecha', 'entr_id', 'dama_horario_id')
    list_filter = ('clas_fecha', 'dama_horario_id', 'entr_id')
    search_fields = ('clas_nombre',)
    date_hierarchy = 'clas_fecha'
    ordering = ('-clas_fecha', 'clas_nombre')


@admin.register(AsistenciaClase)
class AsistenciaClaseAdmin(admin.ModelAdmin):
    list_display = ('ascl_id', 'clie_id', 'clas_id')
    list_filter = ('clas_id', 'clie_id')
    search_fields = ('clie_id__clie_nombre', 'clas_id__clas_nombre')
    ordering = ('-ascl_id',)


@admin.register(ClienteMembresia)
class ClienteMembresiaAdmin(admin.ModelAdmin):
    list_display = ('clme_id', 'clie_id', 'dama_membresia_id', 'clime_fecha_inicio', 'clime_fecha_fin', 'esta_activa')
    list_filter = ('dama_membresia_id', 'clime_fecha_inicio', 'clime_fecha_fin')
    search_fields = ('clie_id__clie_nombre',)
    date_hierarchy = 'clime_fecha_inicio'
    ordering = ('-clime_fecha_inicio',)


@admin.register(EspecialidadEntrenador)
class EspecialidadEntrenadorAdmin(admin.ModelAdmin):
    list_display = ('esen_id', 'entr_id', 'dama_especialidad_id')
    list_filter = ('dama_especialidad_id', 'entr_id')
    search_fields = ('entr_id__entr_nombre',)
    ordering = ('entr_id',)
