from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, PedidoProducto, Producto
from .forms import PedidoForm, PedidoProductoFormSet
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST

def pedido_list(request):
    # Obtener todos los pedidos inicialmente
    pedidos = Pedido.objects.all()  
    
    # Obtener el estado seleccionado del formulario
    estado_seleccionado = request.GET.get('estado')
    
    # Filtrar los pedidos por estado si se ha seleccionado uno
    if estado_seleccionado:
        pedidos = pedidos.filter(estado=estado_seleccionado)

    # Obtener los estados únicos de las opciones definidas en el modelo
    estados_unicos = Pedido.ESTADO_OPCIONES

    return render(request, 'pedidos/pedido_list.html', {
        'pedidos': pedidos,
        'estados_unicos': estados_unicos,  # Pasar las opciones de estado al contexto
        'estado_seleccionado': estado_seleccionado,  # Para mantener la selección en el formulario
    })


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
        producto_formset = PedidoProductoFormSet(request.POST, prefix='pedidoproducto_set')
        
        if pedido_form.is_valid() and producto_formset.is_valid():
            pedido = pedido_form.save(commit=False)

            cliente = pedido_form.cleaned_data.get('cliente')
            if cliente:
                pedido.cliente = cliente
            else:
                print("No se seleccionó cliente correctamente")
            
            # Asignar estado (por defecto "en espera" si no se selecciona ninguno)
            estado = pedido_form.cleaned_data.get('estado')
            if not estado:
                pedido.estado = 'en_espera'
            else:
                pedido.estado = estado

            pedido.precio_total = 0  
            pedido.save()

            for producto_form in producto_formset:
                producto = producto_form.cleaned_data.get('producto')
                cantidad = producto_form.cleaned_data.get('cantidad')
                
                if producto and cantidad:
                    PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)
                    pedido.precio_total += producto.costo * cantidad  

            pedido.save()

            return redirect('pedido_list')
        else:
            # Imprimir los errores en la consola
            print("Errores en el formulario de pedido:", pedido_form.errors)
            print("Errores en el formset de productos:", producto_formset.errors)
    else:
        pedido_form = PedidoForm()
        producto_formset = PedidoProductoFormSet(prefix='pedidoproducto_set')

    
    return render(request, 'pedidos/pedido_form.html', {
        'pedido_form': pedido_form,
        'producto_formset': producto_formset,
    })



def nuevo_pedido(request):
    productos = Producto.objects.all()
    return render(request, 'nuevo_pedido.html', {'productos': productos})

def get_productos(request):
    productos = Producto.objects.all()
    data = [{'id': p.id, 'nombre': p.nombre, 'costo': p.costo, 'porcentaje_ganancia': p.porcentaje_ganancia} for p in productos]
    return JsonResponse(data, safe=False)