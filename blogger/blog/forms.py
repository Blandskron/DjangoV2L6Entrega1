from django import forms
from .models import Articulo, Autor

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'autor']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'biografia']
