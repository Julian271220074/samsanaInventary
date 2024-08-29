
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  Compra
from .forms import  CompraForm
from gestionar_proveedor.models import Proveedor

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gestionar_compra(request):
    compras = Compra.objects.all()
    return render(request, 'gestionar_compra.html', {'compras': compras})



@login_required
def añadir_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra añadida con éxito.')
            return redirect('gestionar_compra')
    else:
        form = CompraForm()
    return render(request, 'añadir_compra.html', {'form': form})



@login_required
def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra actualizada con éxito.')
            return redirect('gestionar_compra')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'editar_compra.html', {'form': form, 'compra': compra})



@login_required
def activar_inactivar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    compra.estado = not compra.estado
    compra.save()
    messages.success(request, f'Compra {compra.estado == True} con éxito.')
    return redirect('gestionar_compra')



@login_required
def consultar_compra(request):
    if request.method == 'POST':
        id_compra = request.POST.get('id_compra')
        fecha_compra = request.POST.get('fecha_compra')
        proveedor = request.POST.get('proveedor')
        estado = request.POST.get('estado')
        
        compras = Compra.objects.all()
        if id_compra:
            compras = compras.filter(id=id_compra)
        if fecha_compra:
            compras = compras.filter(fechaCompra__date=fecha_compra)
        if proveedor:
            compras = compras.filter(proveedorId__nombre__icontains=proveedor)
        if estado:
            compras = compras.filter(estadoCompra=estado)
        
        return render(request, 'consultar_compra.html', {'compras': compras})
    return render(request, 'consultar_compra.html')

def filtrar_compras(request):
    estado_filtro = request.GET.get('estado', None)
    fecha = request.GET.get('fecha', None)
    proveedor_id = request.GET.get('proveedor', '')

    compras = Compra.objects.all()

    if estado_filtro == 'activado':
        compras = compras.filter(estado=True)
    elif estado_filtro == 'inactivado':
        compras = compras.filter(estado=False)

    if fecha:
        compras = compras.filter(fecha_Compra__date=fecha)
    
    if proveedor_id:
        compras = compras.filter(proveedor_Id_id=proveedor_id)

    context = {
        'compras': compras,
        'proveedores': Proveedor.objects.all()
    }

    return render(request, 'gestionar_compra.html', context)