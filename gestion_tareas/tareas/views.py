from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea, Incidencia
from .forms import TareaForm, IncidenciaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# ========================================
# LISTADO PRINCIPAL
# ========================================
@login_required
def lista_tareas(request):
    # Si es responsable/admin, ve todas las tareas e incidencias
    if request.user.is_staff or request.user.is_superuser:
        tareas = Tarea.objects.all()
        incidencias = Incidencia.objects.all().order_by('-fecha_creacion')
    else:  # Clientes solo ven lo suyo
        tareas = Tarea.objects.filter(usuario=request.user)
        incidencias = Incidencia.objects.filter(cliente=request.user).order_by('-fecha_creacion')

    return render(request, 'tareas/lista.html', {
        'tareas': tareas,
        'incidencias': incidencias,
        'is_admin': request.user.is_staff or request.user.is_superuser
    })

# ========================================
# TAREAS
# ========================================
@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()

    return render(request, 'tareas/form.html', {'form': form})


@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'tareas/form.html', {'form': form})


@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    tarea.delete()
    return redirect('lista_tareas')

# ========================================
# INCIDENCIAS
# ========================================
@login_required
def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, request.FILES)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.cliente = request.user
            incidencia.save()
            return redirect('incidencia_enviada')
    else:
        form = IncidenciaForm()

    return render(request, 'incidencias/crear_incidencia.html', {'form': form})


@login_required
def editar_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)

    # Solo admin o staff puede editar
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('lista_tareas')

    if request.method == 'POST':
        form = IncidenciaForm(request.POST, request.FILES, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = IncidenciaForm(instance=incidencia)

    return render(request, 'incidencias/crear_incidencia.html', {
        'form': form,
        'editar': True
    })


@login_required
def eliminar_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)

    # Solo admin o staff puede eliminar
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('lista_tareas')

    incidencia.delete()
    return redirect('lista_tareas')

@login_required
def asignar_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)

    # Solo administradores o staff pueden asignar
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('lista_tareas')

    if request.method == 'POST':
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            messages.success(request, "Incidencia asignada correctamente")
            return redirect('lista_tareas')
    else:
        form = IncidenciaForm(instance=incidencia)

    return render(request, 'incidencias/asignar_incidencia.html', {'form': form, 'incidencia': incidencia})
# Confirmación de incidencia enviada
@login_required
def incidencia_enviada(request):
    return render(request, 'incidencias/incidencia_enviada.html')


# Mostrar lista de incidencias (solo para cliente)
@login_required
def lista_incidencias(request):
    incidencias = Incidencia.objects.filter(cliente=request.user).order_by('-fecha_creacion')
    return render(request, 'incidencias/lista_incidencias.html', {'incidencias': incidencias})


# ========================================
# AUTENTICACIÓN
# ========================================
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect('lista_tareas')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'registration/login.html')