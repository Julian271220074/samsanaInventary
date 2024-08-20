"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include('gestionar_categoria.urls')),
    path('', include('gestionar_compra.urls')),
    path('', include('gestionar_marca.urls')),
    path('', include('gestionar_presentacion.urls')),
    path('', include('gestionar_productos.urls')),
    path('', include('gestionar_ventas.urls')),
    path('', include('gestionar_usuarios.urls')),
    path('', include('gestionar_proveedor.urls')),
    path('', include('gestionar_respaldo.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]