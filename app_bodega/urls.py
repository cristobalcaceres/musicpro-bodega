from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # Entra directo al panel principal
    path('inventario/', views.inventario, name='inventario'),
]