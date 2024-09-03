from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, PedidoProducto, Producto
from .forms import PedidoForm, PedidoProductoFormSet
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST


def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    productos_pedido = PedidoProducto.objects.filter(pedido=pedido)
    
    return render(request, 'pedidos/pedido_detail.html', {
        'pedido': pedido,
        'productos_pedido': productos_pedido
    })

@require_POST
def pedido_delete(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
        pedido.delete()
        return JsonResponse({'status': 'success'})
    except Pedido.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Este pedido no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def pedido_create(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        producto_formset = PedidoProductoFormSet(request.POST)
        
        if pedido_form.is_valid() and producto_formset.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.precio_total = 0  # Inicializamos el precio total en 0
            
            for producto_form in producto_formset:
                producto = producto_form.cleaned_data.get('producto')
                cantidad = producto_form.cleaned_data.get('cantidad')
                
                if producto and cantidad:
                    pedido.precio_total += producto.costo * cantidad  # Sumamos el costo de cada producto
            
            pedido.save()  # Guardamos el pedido con el precio total calculado
            producto_formset.instance = pedido
            producto_formset.save()
            return redirect('pedido_list')
    else:
        pedido_form = PedidoForm()
        producto_formset = PedidoProductoFormSet()
        productos = Producto.objects.all()
    
    return render(request, 'pedidos/pedido_form.html', {
        'pedido_form': pedido_form,
        'producto_formset': producto_formset,
        'productos': productos,
    })

def nuevo_pedido(request):
    productos = Producto.objects.all()
    return render(request, 'nuevo_pedido.html', {'productos': productos})



def get_productos(request):
    productos = Producto.objects.all()
    data = [{'id': p.id, 'nombre': p.nombre, 'costo': p.costo, 'porcentaje_ganancia': p.porcentaje_ganancia} for p in productos]
    return JsonResponse(data, safe=False)