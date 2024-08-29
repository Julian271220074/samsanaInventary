from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('marca/', views.gestionar_marca, name='gestionar_marca'),
    path('marca/añadir/', views.añadir_marca, name='añadir_marca'),
    path('marca/editar/<int:marca_id>/', views.editar_marca, name='editar_marca'),
    path('marca/activar-inactivar/<int:marca_id>/', views.activar_inactivar_marca, name='activar_inactivar_marca'),
<<<<<<< HEAD
    path('marcas/', views.filtrar_marcas, name='filtrar_marcas'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('marca/consultar/', views.consultar_marca, name='consultar_marca'),
    path('eliminar_marca/<int:marca_id>/', views.eliminar_marca, name='eliminar_marca'),
]
>>>>>>> a44fc48c1da68c7d685486a7adda0a954c3ea77c
