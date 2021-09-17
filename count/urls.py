from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cincuenta', views.cincuenta, name="cincuenta"),
    path('tabla', views.tabla, name="tabla"),
  
]
