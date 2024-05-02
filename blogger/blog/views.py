from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from .forms import ArticuloForm, AutorForm

def articulos_list(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/articulos_list.html', {'articulos': articulos})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_list')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})


def detalle_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_list')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})
