from django.shortcuts import render
from django.db.models import Count, Sum
from django.utils.timezone import now
from pedidos.models import Cliente, Pedido, Producto, PedidoProducto

def dashboard_view(request):

    # Consulta de productos más vendidos
    productos_vendidos = PedidoProducto.objects.values('producto__nombre').annotate(total_vendido=Sum('cantidad')).order_by('-total_vendido')[:5]
    
    # Consultar los clientes con más pedidos
    clientes_top = Pedido.objects.values('cliente__nombre').annotate(cantidad_pedidos=Count('id')).order_by('-cantidad_pedidos')[:5]
    
    # Obtener el mes actual y el año actual
    today = now()
    current_month = today.month
    current_year = today.year

    # Consultar pedidos hechos este mes
    pedidos_mes = Pedido.objects.filter(fecha__month=current_month).aggregate(
        total_pedidos=Count('id'),
        total_ventas=Sum('precio_total')  # Cambiar 'total' por 'precio_total'
    )

    # Consultar pedidos hechos este año
    pedidos_anio = Pedido.objects.filter(fecha__year=current_year).aggregate(
        total_pedidos=Count('id'),
        total_ventas=Sum('precio_total')  # Cambiar 'total' por 'precio_total'
    )

    # Consultar cantidad de pedidos pendientes
    pedidos_pendientes = Pedido.objects.filter(estado='en espera').count()
    pedidos_totales = Pedido.objects.all().count()

    # Crear el contexto con todos los datos
    context = {
        'productos_vendidos': productos_vendidos,
        'pedidos_totales': pedidos_totales,
        'clientes_top': clientes_top,
        'pedidos_mes': pedidos_mes,
        'pedidos_anio': pedidos_anio,
        'pedidos_pendientes': pedidos_pendientes,
    }

    return render(request, 'reportes/rep_dashboard.html', context)
