from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import Producto, ProductoForm

def productos_list(request):
    productos = Producto.objects.all()
    return render(request,'productos/producto_list.html',{'productos': productos})

def productos_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            tipo_medida = request.POST.get('tipo_medida_hidden')
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