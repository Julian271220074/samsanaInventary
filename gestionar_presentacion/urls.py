from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('presentacion/', views.gestionar_presentacion, name='gestionar_presentacion'),
    path('presentacion/añadir/', views.añadir_presentacion, name='añadir_presentacion'),
    path('presentacion/editar/<int:presentacion_id>/', views.editar_presentacion, name='editar_presentacion'),
    path('presentacion/activar-inactivar/<int:presentacion_id>/', views.activar_inactivar_presentacion, name='activar_inactivar_presentacion'),
    path('presentacion/consultar/', views.consultar_presentacion, name='consultar_presentacion'),
    path('eliminar_presentacion/<int:presentacion_id>/', views.eliminar_presentacion, name='eliminar_presentacion'),
]