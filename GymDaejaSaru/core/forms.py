from django import forms
from .models import (
    Entrenador, Cliente, Clase, AsistenciaClase,
    ClienteMembresia, EspecialidadEntrenador, DatosMaestros
)


class EntrenadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo tipos de documento (hijos de TIPO_DOCUMENTOS)
        tipo_doc_padre = DatosMaestros.objects.filter(
            dama_nombre='TIPO_DOCUMENTOS'
        ).first()
        if tipo_doc_padre:
            self.fields['dama_tipo_documento'].queryset = DatosMaestros.objects.filter(
                dama_padre_id=tipo_doc_padre,
                dama_estado=1
            )
        else:
            self.fields['dama_tipo_documento'].queryset = DatosMaestros.objects.filter(
                dama_estado=1
            )
        self.fields['dama_tipo_documento'].empty_label = "Seleccione un tipo de documento"

    class Meta:
        model = Entrenador
        fields = [
            'entr_nombre', 'entr_fecha_nacimiento', 'entr_telefono',
            'entr_direccion', 'entr_numero_documento', 'dama_tipo_documento'
        ]
        widgets = {
            'entr_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo'
            }),
            'entr_fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'entr_telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }),
            'entr_direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'entr_numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento'
            }),
            'dama_tipo_documento': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo tipos de documento (hijos de TIPO_DOCUMENTOS)
        tipo_doc_padre = DatosMaestros.objects.filter(
            dama_nombre='TIPO_DOCUMENTOS'
        ).first()
        if tipo_doc_padre:
            self.fields['dama_tipo_documento'].queryset = DatosMaestros.objects.filter(
                dama_padre_id=tipo_doc_padre,
                dama_estado=1
            )
        else:
            self.fields['dama_tipo_documento'].queryset = DatosMaestros.objects.filter(
                dama_estado=1
            )
        self.fields['dama_tipo_documento'].empty_label = "Seleccione un tipo de documento"

    class Meta:
        model = Cliente
        fields = [
            'clie_nombre', 'clie_fecha_nacimiento', 'clie_telefono',
            'clie_direccion', 'clie_numero_documento', 'dama_tipo_documento'
        ]
        widgets = {
            'clie_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo'
            }),
            'clie_fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'clie_telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }),
            'clie_direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'clie_numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento'
            }),
            'dama_tipo_documento': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class ClaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo horarios (hijos de TIPO_HORARIO)
        horario_padre = DatosMaestros.objects.filter(
            dama_nombre='TIPO_HORARIO'
        ).first()
        if horario_padre:
            self.fields['dama_horario_id'].queryset = DatosMaestros.objects.filter(
                dama_padre_id=horario_padre,
                dama_estado=1
            )
        else:
            self.fields['dama_horario_id'].queryset = DatosMaestros.objects.filter(
                dama_estado=1
            )
        self.fields['dama_horario_id'].empty_label = "Seleccione un horario"

    class Meta:
        model = Clase
        fields = ['clas_nombre', 'clas_fecha', 'entr_id', 'dama_horario_id']
        widgets = {
            'clas_nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la clase'
            }),
            'clas_fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'entr_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dama_horario_id': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class AsistenciaClaseForm(forms.ModelForm):
    class Meta:
        model = AsistenciaClase
        fields = ['clas_id', 'clie_id']
        widgets = {
            'clas_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'clie_id': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class ClienteMembresiaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo tipos de membresía (hijos de TIPO_MEMBRESIAS)
        membresia_padre = DatosMaestros.objects.filter(
            dama_nombre='TIPO_MEMBRESIAS'
        ).first()
        if membresia_padre:
            self.fields['dama_membresia_id'].queryset = DatosMaestros.objects.filter(
                dama_padre_id=membresia_padre,
                dama_estado=1
            )
        else:
            self.fields['dama_membresia_id'].queryset = DatosMaestros.objects.filter(
                dama_estado=1
            )
        self.fields['dama_membresia_id'].empty_label = "Seleccione un tipo de membresía"
        
        # Si es una nueva membresía, ocultar los campos de fecha (se establecerán automáticamente)
        if not self.instance.pk:
            self.fields['clime_fecha_inicio'].widget = forms.HiddenInput()
            self.fields['clime_fecha_fin'].widget = forms.HiddenInput()
            self.fields['clime_fecha_inicio'].required = False
            self.fields['clime_fecha_fin'].required = False

    class Meta:
        model = ClienteMembresia
        fields = [
            'clie_id', 'dama_membresia_id',
            'clime_fecha_inicio', 'clime_fecha_fin'
        ]
        widgets = {
            'clie_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dama_membresia_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'clime_fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'clime_fecha_fin': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class EspecialidadEntrenadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo especialidades (hijos de algún padre de especialidades)
        # Asumiendo que hay un padre llamado "ESPECIALIDADES" o similar
        especialidad_padre = DatosMaestros.objects.filter(
            dama_nombre__icontains='ESPECIALIDAD'
        ).first()
        if especialidad_padre:
            self.fields['dama_especialidad_id'].queryset = DatosMaestros.objects.filter(
                dama_padre_id=especialidad_padre,
                dama_estado=1
            )
        else:
            # Si no existe, mostrar todos los datos maestros activos que tengan padre
            self.fields['dama_especialidad_id'].queryset = DatosMaestros.objects.filter(
                dama_padre_id__isnull=False,
                dama_estado=1
            )
        self.fields['dama_especialidad_id'].empty_label = "Seleccione una especialidad"

    class Meta:
        model = EspecialidadEntrenador
        fields = ['entr_id', 'dama_especialidad_id']
        widgets = {
            'entr_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dama_especialidad_id': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

