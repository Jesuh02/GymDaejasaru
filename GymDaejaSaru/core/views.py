from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Entrenador, Cliente, Clase, AsistenciaClase,
    ClienteMembresia, EspecialidadEntrenador, DatosMaestros
)
from .forms import (
    EntrenadorForm, ClienteForm, ClaseForm, AsistenciaClaseForm,
    ClienteMembresiaForm, EspecialidadEntrenadorForm
)


def home(request):
    """Vista principal del sistema"""
    context = {
        'total_entrenadores': Entrenador.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_clases': Clase.objects.count(),
        'total_membresias': ClienteMembresia.objects.count(),
    }
    return render(request, 'core/home.html', context)


# ========== ENTRENADORES ==========
class EntrenadorListView(ListView):
    model = Entrenador
    template_name = 'core/entrenadores/list.html'
    context_object_name = 'entrenadores'
    paginate_by = 10

    def get_queryset(self):
        queryset = Entrenador.objects.select_related('dama_tipo_documento').all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(entr_nombre__icontains=search)
        return queryset


def entrenador_create(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador creado exitosamente.')
            return redirect('entrenador_list')
    else:
        form = EntrenadorForm()
    return render(request, 'core/entrenadores/form.html', {'form': form, 'title': 'Crear Entrenador'})


def entrenador_update(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador actualizado exitosamente.')
            return redirect('entrenador_list')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'core/entrenadores/form.html', {'form': form, 'title': 'Editar Entrenador', 'object': entrenador})


def entrenador_delete(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        entrenador.delete()
        messages.success(request, 'Entrenador eliminado exitosamente.')
        return redirect('entrenador_list')
    return render(request, 'core/entrenadores/delete.html', {'object': entrenador})


# ========== CLIENTES ==========
class ClienteListView(ListView):
    model = Cliente
    template_name = 'core/clientes/list.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = Cliente.objects.select_related('dama_tipo_documento').all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(clie_nombre__icontains=search)
        return queryset


def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'core/clientes/form.html', {'form': form, 'title': 'Crear Cliente'})


def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/clientes/form.html', {'form': form, 'title': 'Editar Cliente', 'object': cliente})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('cliente_list')
    return render(request, 'core/clientes/delete.html', {'object': cliente})


# ========== CLASES ==========
class ClaseListView(ListView):
    model = Clase
    template_name = 'core/clases/list.html'
    context_object_name = 'clases'
    paginate_by = 10

    def get_queryset(self):
        queryset = Clase.objects.select_related('entr_id', 'dama_horario_id').all()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(clas_nombre__icontains=search)
        return queryset


def clase_create(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase creada exitosamente.')
            return redirect('clase_list')
    else:
        form = ClaseForm()
    return render(request, 'core/clases/form.html', {'form': form, 'title': 'Crear Clase'})


def clase_update(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase actualizada exitosamente.')
            return redirect('clase_list')
    else:
        form = ClaseForm(instance=clase)
    return render(request, 'core/clases/form.html', {'form': form, 'title': 'Editar Clase', 'object': clase})


def clase_delete(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        clase.delete()
        messages.success(request, 'Clase eliminada exitosamente.')
        return redirect('clase_list')
    return render(request, 'core/clases/delete.html', {'object': clase})


# ========== ASISTENCIAS ==========
class AsistenciaClaseListView(ListView):
    model = AsistenciaClase
    template_name = 'core/asistencias/list.html'
    context_object_name = 'asistencias'
    paginate_by = 10

    def get_queryset(self):
        return AsistenciaClase.objects.select_related('clas_id', 'clie_id').all()


def asistencia_create(request):
    if request.method == 'POST':
        form = AsistenciaClaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia registrada exitosamente.')
            return redirect('asistencia_list')
    else:
        form = AsistenciaClaseForm()
    return render(request, 'core/asistencias/form.html', {'form': form, 'title': 'Registrar Asistencia'})


def asistencia_delete(request, pk):
    asistencia = get_object_or_404(AsistenciaClase, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Asistencia eliminada exitosamente.')
        return redirect('asistencia_list')
    return render(request, 'core/asistencias/delete.html', {'object': asistencia})


# ========== MEMBRESÍAS ==========
class ClienteMembresiaListView(ListView):
    model = ClienteMembresia
    template_name = 'core/membresias/list.html'
    context_object_name = 'membresias'
    paginate_by = 10

    def get_queryset(self):
        return ClienteMembresia.objects.select_related('clie_id', 'dama_membresia_id').all()


def membresia_create(request):
    if request.method == 'POST':
        form = ClienteMembresiaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membresía creada exitosamente.')
            return redirect('membresia_list')
    else:
        form = ClienteMembresiaForm()
    return render(request, 'core/membresias/form.html', {'form': form, 'title': 'Crear Membresía'})


def membresia_update(request, pk):
    membresia = get_object_or_404(ClienteMembresia, pk=pk)
    if request.method == 'POST':
        form = ClienteMembresiaForm(request.POST, instance=membresia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membresía actualizada exitosamente.')
            return redirect('membresia_list')
    else:
        form = ClienteMembresiaForm(instance=membresia)
    return render(request, 'core/membresias/form.html', {'form': form, 'title': 'Editar Membresía', 'object': membresia})


def membresia_delete(request, pk):
    membresia = get_object_or_404(ClienteMembresia, pk=pk)
    if request.method == 'POST':
        membresia.delete()
        messages.success(request, 'Membresía eliminada exitosamente.')
        return redirect('membresia_list')
    return render(request, 'core/membresias/delete.html', {'object': membresia})


# ========== ESPECIALIDADES ==========
class EspecialidadEntrenadorListView(ListView):
    model = EspecialidadEntrenador
    template_name = 'core/especialidades/list.html'
    context_object_name = 'especialidades'
    paginate_by = 10

    def get_queryset(self):
        return EspecialidadEntrenador.objects.select_related('entr_id', 'dama_especialidad_id').all()


def especialidad_create(request):
    if request.method == 'POST':
        form = EspecialidadEntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especialidad asignada exitosamente.')
            return redirect('especialidad_list')
    else:
        form = EspecialidadEntrenadorForm()
    return render(request, 'core/especialidades/form.html', {'form': form, 'title': 'Asignar Especialidad'})


def especialidad_delete(request, pk):
    especialidad = get_object_or_404(EspecialidadEntrenador, pk=pk)
    if request.method == 'POST':
        especialidad.delete()
        messages.success(request, 'Especialidad eliminada exitosamente.')
        return redirect('especialidad_list')
    return render(request, 'core/especialidades/delete.html', {'object': especialidad})
