from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Proveedor
from .forms import Producto, ProductoForm, ProductoUpdateForm,CargarExcelForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
import pandas as pd
from decimal import Decimal

def productos_list(request):
    categoria_id = request.GET.get('categoria')  # Obtén la categoría de los parámetros de consulta
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)  
    else:
        productos = Producto.objects.all()  
    categorias = Categoria.objects.all()  
    return render(request,'productos/producto_list.html',{'productos': productos, 'categorias':categorias})

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
            print(form.errors)
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
            'precio_actual': producto.precio, 
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
        print(f"Producto ID: {producto_id}")
        producto = get_object_or_404(Producto, pk=producto_id)
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente')
            return redirect('producto_list')  # Redirige a la lista de productos después de la actualización
        else:
            print(form.errors)
    else:
        form = ProductoUpdateForm()
    
    return render(request, 'productos/producto_update.html', {'producto_form': form})

def productos_upload_excel(request):
    if request.method == 'POST':
        form = CargarExcelForm(request.POST, request.FILES)
        if form.is_valid():
            if 'archivo' in request.FILES:
                print(f"Archivo cargado: {request.FILES['archivo'].name}")
            else:
                print("No se ha seleccionado ningún archivo.")
                
            if 'archivo' not in request.FILES:
                messages.error(request, 'No se ha seleccionado ningún archivo.')
                return redirect('producto_list')

            excel_file = request.FILES['archivo']

            try:
                print(f"Archivo cargado: {request.FILES['archivo'].name}")
                df = pd.read_excel(excel_file, engine='openpyxl')

                df.columns = df.columns.str.strip().str.lower()

                required_columns = ['nombre', 'categoria','proveedor','costo', 'cantidad', 'porcentaje_ganancia', 'tipo_medida']
                if not all(col in df.columns for col in required_columns):
                    messages.error(request, 'El archivo Excel no contiene las columnas requeridas.')
                    return redirect('producto_list')

               
                for _, row in df.iterrows():
                    try:
                        categoria = Categoria.objects.get(nombre=row['categoria'])  
                    except Categoria.DoesNotExist:
                        messages.error(request, f'Categoría no encontrada: {row["categoria"]}')
                        return redirect('producto_list')
                    try:
                        proveedor = Proveedor.objects.get(nombre=row['proveedor'])  
                    except Proveedor.DoesNotExist:
                        messages.error(request, f'Proveedor no encontrado: {row["proveedor"]}')
                        return redirect('producto_list')

                    tipo_medida = row['tipo_medida']
                    if tipo_medida not in dict(Producto.TIPO_MEDIDA_CHOICES):
                        messages.error(request, f'Tipo de medida inválido: {tipo_medida}')
                        return redirect('producto_list')

                    producto = Producto(
                        nombre=row['nombre'],
                        categoria=categoria,
                        proveedor=proveedor,
                        costo=row['costo'],
                        cantidad=row['cantidad'],
                        porcentaje_ganancia=row['porcentaje_ganancia'],
                        tipo_medida=tipo_medida
                    )
                    producto.save()

                messages.success(request, 'Productos cargados exitosamente.')
                return redirect('producto_list')

            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')
                return redirect('producto_list')
        else:
            messages.error(request, 'No se ha seleccionado ningún archivo.')
            print("El archivo no esta cargando aca")
    else:
        form = CargarExcelForm()

    return render(request, 'productos/producto_form.html', {'form': form})


def update_masivo(request):
    if request.method == 'POST':
        productos = Producto.objects.all()
        categoria_id = request.POST.get('categoria')  
        porcentaje_aumento = request.POST.get('porcentaje_aumento')
        porcentaje_aumento = Decimal(porcentaje_aumento)

        if categoria_id:
            productos = productos.filter(categoria_id=categoria_id)  
        if porcentaje_aumento:
            try:
                for producto in productos:
                    producto.costo += (producto.costo * porcentaje_aumento / 100)
                    producto.save()
                messages.success(request, f'Precios actualizados exitosamente con un aumento del {porcentaje_aumento}% para los productos seleccionados.')
            except ValueError:
                messages.error(request, 'Por favor, ingrese un valor numérico válido para el porcentaje de aumento.')
        else:
            messages.error(request, 'Por favor, ingrese un porcentaje de aumento.')
        
        return redirect('producto_list')
    
    else:
        categorias = Categoria.objects.all()  # Para el menú desplegable de categorías
        return render(request, 'productos/producto_update_masivo.html', {'categorias': categorias})