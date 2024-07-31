from django.urls import path
from playworksapp import views

urlpatterns = [
    path("", views.inicio),
    path("contacto/", views.ContactoCreateView.as_view(), name="CrearContactos"),
    path("clientes/", views.ClienteListView.as_view(), name="ListarClientes"),
    path("empleo/", views.EmpleoDetailView.as_view(), name="DetallarEmpleos"),
    path("formulario/", views.FormularioListView.as_view(), name="ListarFormularios"),
    path("busquedaCliente/", views.busquedaCliente, name="BusquedaCliente"),
    path('buscar/', views.buscar),
]
