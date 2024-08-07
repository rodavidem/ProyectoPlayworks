from django.urls import path
from playworksapp import views

urlpatterns = [
    path("", views.inicio),
    path("contacto/", views.ContactoCreateView.as_view(), name="CrearContactos"),
    path("clientes/", views.ClienteListView.as_view(), name="ListarClientes"),
    path("empleo/", views.EmpleoListView.as_view(), name="DetallarEmpleos"),
    path("formulario/", views.FormularioListView.as_view(), name="ListarFormularios"),
    path('buscar/', views.buscar, name='buscar'),
    path('resultados/', views.resultados, name='resultados'),
]
