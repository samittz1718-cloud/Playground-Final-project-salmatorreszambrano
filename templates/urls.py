from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('listar/', views.listar_clientes, name='listar_clientes'),
]
