from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from playworksapp.models import Contacto, Empleo, Formulario, Cliente
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "playworksapp/index.html")

def busquedaCliente(request):

    return render(request, "playworksapp/busquedaCliente.html")

def buscar(request):

    if request.GET["nombre"]:
        respuesta = f"Estoy buscando al cliente: {request.GET['nombre'] }"
        nombre = request.GET["nombre"]

    else:

        respuesta = "No enviaste datos"
        
    return HttpResponse(respuesta)


class ContactoCreateView(CreateView):
    model = Contacto
    template_name = "playworksapp/contacto.html"
    success_url = reverse_lazy('ListarClientes')
    fields = ['nombre','email','consulta']

class ClienteListView(ListView):
    model = Cliente
    context_object_name = "clientes"
    template_name = "playworksapp/clientes.html"

class EmpleoDetailView(DetailView):
    model = Empleo
    context_object_name = "empleos"
    template_name = "playworksapp/empleo.html"

class FormularioListView(ListView):
    model = Formulario
    template_name = "playworksapp/formulario.html"
    success_url = reverse_lazy('ListarClientes')
    fields = ['nombre','email','consulta']