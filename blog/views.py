from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

def home(request):
    return render(request, 'home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'form.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'form.html', {'form': form, 'titulo': 'Crear Categoria'})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'form.html', {'form': form, 'titulo': 'Crear Post'})

def buscar_post(request):
    form = BuscarPostForm(request.GET or None)
    resultados = None
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        resultados = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})
