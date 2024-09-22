from django.db import models
from django.shortcuts import render

def dashboard_view(request):
    # Lógica para el dashboard
    return render(request, 'dashboard.html')


# Create your models here.
