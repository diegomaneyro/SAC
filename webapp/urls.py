"""
Este módulo contiene las rutas de URL para la aplicación web.
"""

from django.urls import path
from . import views

# Lista de URL de la aplicación web para importar al proyecto
urlpatterns = [   
    # Página de inicio
    path('', views.inicio),
    
    # Página "Acerca de"
    path('about/', views.about),
]
