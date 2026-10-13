import os
import django
import random
import uuid
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicpro_site.settings')
django.setup()

from app_bodega.models import Categoria, Producto

fake = Faker('es_CL')

def poblar_bd(cantidad=100):
    print(f"Generando {cantidad} registros...")
    
    categorias = ['Audio', 'Iluminación', 'Escenografía', 'Cableado', 'Energía', 'Video']
    cat_objs = [Categoria.objects.get_or_create(nombre=c)[0] for c in categorias]

    productos = []
    for _ in range(cantidad):
        stock_act = random.randint(0, 100)
        stock_min = random.randint(5, 20)
        
        # Se agrega uuid para garantizar que el código sea 100% único y nunca choque
        codigo_unico = f"MPT-{fake.lexify('???').upper()}-{uuid.uuid4().hex[:6].upper()}"
        
        prod = Producto(
            codigo=codigo_unico,
            nombre=fake.catch_phrase(),
            categoria=random.choice(cat_objs),
            stock=stock_act,
            stock_minimo=stock_min,
            ubicacion=f"Bodega {random.choice(['A','B','C'])}",
            estado='CRITICO' if stock_act < stock_min else 'OPTIMO'
        )
        productos.append(prod)
    
    Producto.objects.bulk_create(productos)
    print("¡Carga exitosa!")

if __name__ == '__main__':
    poblar_bd(1000)