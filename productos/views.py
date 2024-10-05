from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import Producto, ProductoForm, ProductoUpdateForm,CargarExcelForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
import pandas as pd

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
            'stock_actual': producto.cantidad,  
            'precio_actual': producto.costo, 
        }
        return JsonResponse(data)  # Devuelve los datos en formato JSON

    return JsonResponse({'error': 'No es una solicitud AJAX'}, status=400)

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
            messages.success(request, 'Producto actualizado correctamente')
            return redirect('producto_list')  # Redirige a la lista de productos después de la actualización
    else:
        form = ProductoUpdateForm()
    
    return render(request, 'productos/producto_update.html', {'producto_form': form})

def productos_upload_excel(request):
    if request.method == 'POST':
        form = CargarExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']

            try:
                df = pd.read_excel(excel_file, engine='openpyxl')

                required_columns = ['nombre', 'categoria', 'costo', 'cantidad', 'porcentaje_ganancia', 'tipo_medida']
                if not all(col in df.columns for col in required_columns):
                    messages.error(request, 'El archivo Excel no contiene las columnas requeridas.')
                    return redirect('producto_upload_excel')

                # Procesar cada fila del DataFrame y guardar los productos
                for _, row in df.iterrows():
                    categoria = Categoria.objects.get(nombre=row['categoria'])  # Busca la categoría
                    producto = Producto(
                        nombre=row['nombre'],
                        categoria=categoria,
                        costo=row['costo'],
                        cantidad=row['cantidad'],
                        porcentaje_ganancia=row['porcentaje_ganancia'],
                        tipo_medida=row['tipo_medida']
                    )
                    producto.save()

                messages.success(request, 'Productos cargados exitosamente.')
                return redirect('producto_list')

            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')
                return redirect('producto_upload_excel')

    else:
        form = CargarExcelForm()

    return render(request, 'productos/producto_upload_excel.html', {'form': form})