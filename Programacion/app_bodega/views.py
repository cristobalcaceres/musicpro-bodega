from django.shortcuts import render
from django.contrib import messages

# Datos simulados (Mock data) requeridos por el caso
PRODUCTOS_MOCK = [
    {'codigo': 'PRD-001', 'nombre': 'Guitarra Eléctrica Epiphone', 'categoria': 'Cuerdas', 'stock': 15, 'ubicacion': 'Pasillo A-1'},
    {'codigo': 'PRD-002', 'nombre': 'Batería Acústica Pearl', 'categoria': 'Percusión', 'stock': 3, 'ubicacion': 'Pasillo C-2'},
    {'codigo': 'PRD-003', 'nombre': 'Amplificador Marshall', 'categoria': 'Audio', 'stock': 8, 'ubicacion': 'Pasillo B-1'},
]

def dashboard(request):
    messages.info(request, 'Bienvenido al panel de control de la Bodega Central.')
    return render(request, 'bodega/dashboard.html')

def inventario(request):
    productos_procesados = []
    alertas_stock = 0
    
    for prod in PRODUCTOS_MOCK:
        estado = 'Óptimo'
        if prod['stock'] < 5:
            estado = 'Crítico'
            alertas_stock += 1
            
        productos_procesados.append({
            **prod,
            'estado': estado
        })
        
    contexto = {
        'titulo': 'Gestión de Inventario',
        'productos': productos_procesados,
        'total_alertas': alertas_stock
    }
    
    return render(request, 'bodega/inventario.html', contexto)