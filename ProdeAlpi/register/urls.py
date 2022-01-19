from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('prueba/', views.prueba, name='prueba_html'),
]
