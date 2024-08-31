from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import Cliente, ClienteForm
from django.http import JsonResponse
from django.conf import settings
import requests as req

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

def get_paises(request):
    url = f"https://api.countrystatecity.in/v1/countries"
    headers = {'X-CSCAPI-KEY': settings.CSC_API_KEY}
    response = req.get(url, headers=headers)
    data = response.json()
    if response.status_code  == 200:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Error al obtener paises'}, status=400)

def get_provincias(request, pais_iso2):
    url = f"https://api.countrystatecity.in/v1/countries/{pais_iso2}/states"
    headers = {'X-CSCAPI-KEY': settings.CSC_API_KEY}
    response = req.get(url, headers=headers)
    data = response.json()
    if response.status_code  == 200:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Error al obtener provincias'}, status=400)

def get_ciudades(request, pais_iso2, provincia_iso2):
    url = f"https://api.countrystatecity.in/v1/countries/{pais_iso2}/states/{provincia_iso2}/cities"
    headers = {'X-CSCAPI-KEY': settings.CSC_API_KEY}
    response = req.get(url, headers=headers)
    data = response.json()
    if response.status_code  == 200:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Error al obtener ciudades'}, status=400)