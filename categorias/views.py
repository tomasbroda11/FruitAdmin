from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse



def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categoria_list.html', {'categorias': categorias})

def categorias_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_list')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categorias_detail(request,pk):
    categoria = get_object_or_404(Categoria,pk=pk)
    return render(request, 'categorias/categoria_detail.html', {
        'categoria': categoria
    })

@require_POST
def categorias_delete(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return JsonResponse({'status': 'success'})
    except Categoria.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Esta categoria no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)