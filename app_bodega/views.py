from django.shortcuts import render

# Diccionario con los datos del mockup (Evaluación 1)
PRODUCTOS_MOCK = [
    {'codigo': 'MPT-AUD-001', 'nombre': 'Subwoofer Yamaha DXS18', 'categoria': 'Audio', 'stock': 14, 'min': 4, 'ubicacion': 'Bodega A - Rack 3'},
    {'codigo': 'MPT-AUD-002', 'nombre': 'Monitor QSC K12.2', 'categoria': 'Audio', 'stock': 2, 'min': 4, 'ubicacion': 'Bodega A - Rack 4'},
    {'codigo': 'MPT-ILU-003', 'nombre': 'Moving Head Beam 330W', 'categoria': 'Iluminación', 'stock': 22, 'min': 6, 'ubicacion': 'Bodega B - Estante 1'},
    {'codigo': 'MPT-ILU-004', 'nombre': 'Par LED RGBW 18x10W', 'categoria': 'Iluminación', 'stock': 1, 'min': 8, 'ubicacion': 'Bodega B - Estante 2'},
]

def dashboard(request):
    return render(request, 'bodega/dashboard.html')

def inventario(request):
    productos_procesados = []
    alertas = []
    
    for prod in PRODUCTOS_MOCK:
        estado = 'ÓPTIMO'
        if prod['stock'] < prod['min']:
            estado = 'CRÍTICO'
            alertas.append(prod['codigo'])
            
        productos_procesados.append({**prod, 'estado': estado})
        
    contexto = {
        'productos': productos_procesados,
        'alertas': alertas,
        'total_articulos': len(PRODUCTOS_MOCK)
    }
    
    return render(request, 'bodega/inventario.html', contexto)