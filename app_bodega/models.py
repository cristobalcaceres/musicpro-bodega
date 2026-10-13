from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    ESTADOS = (
        ('OPTIMO', 'Óptimo'),
        ('CRITICO', 'Crítico'),
    )
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5)
    ubicacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='OPTIMO')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"