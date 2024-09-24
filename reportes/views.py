from django.shortcuts import render
from django.db.models import Count, Sum
from django.utils.timezone import now
from pedidos.models import Cliente, Pedido, Producto, PedidoProducto
import json
from django.db.models.functions import TruncMonth 

def dashboard_view(request):
    # Consulta de productos más vendidos
    productos_vendidos = PedidoProducto.objects.values('producto__nombre').annotate(total_vendido=Sum('cantidad')).order_by('-total_vendido')[:5]

    # Listas para los nombres de productos y sus cantidades
    nombres_productos = [producto['producto__nombre'] for producto in productos_vendidos]
    cantidades_vendidas = [producto['total_vendido'] for producto in productos_vendidos]

    # Otras consultas de la vista (ya existentes)
    clientes_top = Pedido.objects.values('cliente__nombre').annotate(cantidad_pedidos=Count('id')).order_by('-cantidad_pedidos')[:5]
    
    today = now()
    current_month = today.month
    current_year = today.year
    # Consulta para pedidos por mes
    pedidos_por_mes = Pedido.objects.filter(fecha__year=current_year).annotate(mes=TruncMonth('fecha')).values('mes').annotate(total_pedidos=Count('id')).order_by('mes')
    # Preparar los datos para Chart.js
    meses = [pedido['mes'].strftime('%B') for pedido in pedidos_por_mes]
    pedidos_por_mes_cantidad = [pedido['total_pedidos'] for pedido in pedidos_por_mes]

    pedidos_mes = Pedido.objects.filter(fecha__month=current_month).aggregate(
        total_pedidos=Count('id'),
        total_ventas=Sum('precio_total')
    )

    pedidos_anio = Pedido.objects.filter(fecha__year=current_year).aggregate(
        total_pedidos=Count('id'),
        total_ventas=Sum('precio_total')
    )

    pedidos_pendientes = Pedido.objects.filter(estado='en espera').count()
    pedidos_totales = Pedido.objects.all().count()

    # Contexto actualizado con los nombres y cantidades de productos más vendidos
    context = {
        'productos_vendidos': productos_vendidos,
        'nombres_productos_json': json.dumps(nombres_productos),  # <-- JSON para los nombres
        'cantidades_vendidas_json': json.dumps(cantidades_vendidas),
        'pedidos_totales': pedidos_totales,
        'clientes_top': clientes_top,
        'pedidos_mes': pedidos_mes,
        'pedidos_anio': pedidos_anio,
        'pedidos_pendientes': pedidos_pendientes,
        'meses_json': json.dumps(meses),  # Meses para Chart.js
        'pedidos_por_mes_json': json.dumps(pedidos_por_mes_cantidad),  # Cantidades por mes
    }

    return render(request, 'reportes/rep_dashboard.html', context)
