from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor
from .forms import Proveedor, ProveedorForm, ProveedorUpdateForm
from django.http import JsonResponse
from django.conf import settings
import requests as req
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request,'proveedores/proveedores_list.html',{'proveedores': proveedores})

def proveedores_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    
    return render(request, 'proveedores/proveedor_form.html', {'form': form})

def proveedores_detail(request,pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)
    return render(request, 'proveedores/proveedor_detail.html', {
        'proveedor': proveedor
    })

@require_POST
def proveedores_delete(request, pk):
    try:
        proveedor = Proveedor.objects.get(pk=pk)  # Cambiado a 'Proveedor'
        proveedor.delete()
        return JsonResponse({'status': 'success'})
    except Proveedor.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Este proveedor no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def proveedores_update(request, pk):
    proveedor = get_object_or_404(Proveedor, id=pk)  # Obtiene el proveedor o retorna un 404 si no existe
    if request.method == 'POST':
        form = ProveedorUpdateForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'El proveedor fue actualizado correctamente!')
            return redirect('proveedores_list')  # Redirige a la lista de proveedores o a la vista que prefieras
    else:
        form = ProveedorUpdateForm(instance=proveedor)

    return render(request, 'proveedores/proveedor_update.html', {'form': form, 'proveedores': proveedor})
