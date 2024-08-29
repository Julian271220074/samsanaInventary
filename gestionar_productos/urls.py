from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productos/', views.gestionar_productos, name='gestionar_productos'),
    path('productos/añadir/', views.añadir_producto, name='añadir_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/activar-inactivar/<int:producto_id>/', views.activar_inactivar_producto, name='activar_inactivar_producto'),
    path('productos/consultar/', views.consultar_producto, name='consultar_producto'),
<<<<<<< HEAD
    path('filtrar_productos/', views.filtrar_productos, name='filtrar_productos'),
    
=======
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
>>>>>>> a44fc48c1da68c7d685486a7adda0a954c3ea77c
]