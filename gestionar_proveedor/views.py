from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gestionar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'gestionar_proveedor.html', {'proveedores': proveedores})

@login_required
def añadir_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor añadido con éxito.')
            return redirect('gestionar_proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'añadir_proveedor.html', {'form': form})



@login_required
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado con éxito.')
            return redirect('gestionar_proveedor')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})



@login_required
def activar_inactivar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.estado = not proveedor.estado
    proveedor.save()
    estado = "activado" if proveedor.estado else "inactivado"
    messages.success(request, f'Proveedor {estado} con éxito.')
    return redirect('gestionar_proveedor')



@login_required
def consultar_proveedor(request):
    if request.method == 'POST':
        id_proveedor = request.POST.get('id_proveedor')
        nombre = request.POST.get('nombre')
        producto = request.POST.get('producto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        
        proveedor = None
        if id_proveedor:
            proveedor = Proveedor.objects.filter(id=id_proveedor).first()
        elif nombre:
            proveedor = Proveedor.objects.filter(nombre__icontains=nombre).first()
        elif producto:
            proveedor = Proveedor.objects.filter(producto__icontains=producto).first()
        elif telefono:
            proveedor = Proveedor.objects.filter(telefono__icontains=telefono).first()
        elif email:
            proveedor = Proveedor.objects.filter(email__icontains=email).first()
        elif direccion:
            proveedor = Proveedor.objects.filter(direccion__icontains=direccion).first()
        
        if proveedor:
            return render(request, 'consultar_proveedor.html', {'proveedor': proveedor})
        else:
            messages.error(request, 'Proveedor no encontrado.')
    return render(request, 'consultar_proveedor.html')

@login_required
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente.')
        return redirect('gestionar_proveedor')  

    return render(request, 'confirmar_eliminacion_proveedor.html', {'proveedor': proveedor})

