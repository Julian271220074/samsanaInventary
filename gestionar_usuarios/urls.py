
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('usuarios/añadir/', views.añadir_usuario, name='añadir_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/activar-inactivar/<int:usuario_id>/', views.activar_inactivar_usuario, name='activar_inactivar_usuario'),
    path('usuarios/consultar/', views.consultar_usuario, name='consultar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]