from django.shortcuts import render

def dashboard(request):
    return render(request, 'reportes/rep_dasboard.html')

