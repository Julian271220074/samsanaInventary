from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('compra/', views.gestionar_compra, name='gestionar_compra'),
    path('compra/añadir/', views.añadir_compra, name='añadir_compra'),
    path('compra/editar/<int:compra_id>/', views.editar_compra, name='editar_compra'),
    path('compra/activar-inactivar/<int:compra_id>/', views.activar_inactivar_compra, name='activar_inactivar_compra'),
    path('compras/', views.filtrar_compras, name='filtrar_compras'),
    
    ]