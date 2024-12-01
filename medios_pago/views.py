from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import MedioPago
from .forms import MediospagoForm,MediospagoUpdateForm

def mediospago_list(request):
    mediospago = MedioPago.objects.all()
    return render(request, 'mediospago/mediospago_list.html', {'medios_pago': mediospago})

def mediospago_create(request):
    if request.method == 'POST':
        form = MediospagoForm(request.POST)
        if form.is_valid(): 
            mediopago = form.save(commit=False)
            mediopago.save()
            return redirect('medios_pago_list')
        else:
            print(form.errors)
    else:
        form =MediospagoForm()
    
    return render(request, 'mediospago/mediospago_form.html', {'form': form})

def mediospago_detail(request,pk):
    mediopago = get_object_or_404(MedioPago,pk=pk)
    return render(request, 'mediospago/mediospago_detail.html', {
        'mediospago': mediopago
    })

@require_POST
def mediospago_delete(request, pk):
    try:
        mediopago = MedioPago.objects.get(pk=pk)
        mediopago.delete()
        return JsonResponse({'status': 'success'})
    except MedioPago.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Este medio de pago no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def mediospago_update(request, pk):  
    mediopago = get_object_or_404(MedioPago, pk=pk) 
    if request.method == 'POST':
        form = MediospagoForm(request.POST, instance=mediopago)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medio de pago actualizado correctamente')
            return redirect('medios_pago_list')  
        else:
            print(form.errors)
    else:
        form = MediospagoForm(instance=mediopago)
    return render(request, 'mediospago/mediospago_form.html', {'form': form})