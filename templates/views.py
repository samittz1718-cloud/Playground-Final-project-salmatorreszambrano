from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, CompraForm
from .models import Cliente

def agregar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/formulario.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})
