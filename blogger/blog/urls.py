from django.urls import path
from . import views

urlpatterns = [
    path('', views.articulos_list, name='articulos_list'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('<int:id>/', views.detalle_articulo, name='detalle_articulo'),
]
