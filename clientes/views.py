from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import Cliente, ClienteForm


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes/cliente_list.html',{'clientes': clientes})

def clientes_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/clientes.html', {'form': form})

def clientes_detail(request,pk):
    cliente = get_object_or_404(Cliente,pk=pk)
    return render(request, 'clientes/cliente_detail.html', {
        'cliente': cliente
    })