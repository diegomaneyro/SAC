"""
Este módulo contiene las rutas de URL para la aplicación web.
"""
from django.http import HttpResponse
from django.urls import path
from . import views

# Lista de URL de la aplicación web para importar al proyecto
urlpatterns = [   
    path('', views.index),    
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    
]