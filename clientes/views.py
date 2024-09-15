from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import Cliente, ClienteForm
from django.http import JsonResponse
from django.conf import settings
import requests as req
from django.views.decorators.http import require_POST

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
    
    return render(request, 'clientes/cliente_form.html', {'form': form})

def clientes_detail(request,pk):
    cliente = get_object_or_404(Cliente,pk=pk)
    return render(request, 'clientes/cliente_detail.html', {
        'cliente': cliente
    })

@require_POST
def clientes_delete(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
        return JsonResponse({'status': 'success'})
    except Cliente.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Este cliente no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

