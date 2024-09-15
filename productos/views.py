from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import Producto, ProductoForm, ProductoUpdateForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def productos_list(request):
    productos = Producto.objects.all()
    return render(request,'productos/producto_list.html',{'productos': productos})

def productos_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            tipo_medida = request.POST.get('tipo_medida')
            producto.tipo_medida = tipo_medida
            producto.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/producto_form.html', {'form': form})

def productos_detail(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    return render(request, 'productos/producto_detail.html', {
        'producto': producto
    })

def productos_api_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'stock_actual': producto.cantidad,  # Asegúrate de que 'cantidad' es el campo correcto
            'precio_actual': producto.costo,    # Asegúrate de que 'costo' es el campo correcto
        }
        return JsonResponse(data)
    return render(request, 'productos/producto_detail.html', {
        'producto': producto
    })

@require_POST
def productos_delete(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return JsonResponse({'status': 'success'})
    except Producto.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Este pedido no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
def productos_update(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        producto = get_object_or_404(Producto, pk=producto_id)
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:producto_list')  # Redirige a la lista de productos después de la actualización
    else:
        form = ProductoUpdateForm()
    
    return render(request, 'productos/producto_update.html', {'producto_form': form})