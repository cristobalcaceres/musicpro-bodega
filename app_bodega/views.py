from django.shortcuts import render
from .models import Producto

def dashboard(request):
    return render(request, 'bodega/dashboard.html')

def inventario(request):
    
    productos_db = Producto.objects.all()
    
    
    alertas = [prod.codigo for prod in productos_db if prod.stock < prod.stock_minimo]
        
    contexto = {
        'productos': productos_db,
        'alertas': alertas,
        'total_articulos': productos_db.count()
    }
    
    return render(request, 'bodega/inventario.html', contexto)