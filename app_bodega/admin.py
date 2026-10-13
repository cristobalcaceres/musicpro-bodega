from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'stock', 'stock_minimo', 'ubicacion', 'estado')
    list_filter = ('categoria', 'estado')
    search_fields = ('codigo', 'nombre', 'ubicacion')
    list_editable = ('stock', 'estado')
    