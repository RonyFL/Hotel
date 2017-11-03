from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Empleado
from .models import Book
from .models import Repara
from .models import Consultas
from .models import Factura
from .forms import DatoForm
from .forms import AdministradoresForm
from .forms import LoginForm
from .forms import ConsultaForm
from .forms import TecnicoForm
from .forms import FacturaForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import CrearUsuario

# Create your views here.
class BaseView(TemplateView):
	template_name='base.html'

class SomosView(TemplateView):
    template_name='somos.html'
		
class IndexView(TemplateView):
	template_name='index.html'

class TablaView(TemplateView):
	template_name='tabla.html'

class DatoView(TemplateView):
	template_name='Datos.html'
	
class CrearDatoView(CreateView):
    template_name = 'crearcliente.html'
    form_class = DatoForm
    success_url = reverse_lazy('app1:index')
 
class AdministradoresView(CreateView):
    template_name = 'crearadmin.html'
    form_class = AdministradoresForm
    success_url = reverse_lazy('app1:index')

   
    
class LoginView(FormView):
    template_name = 'Login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('app1:base')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

def LogoutView(request):
    logout(request)
    return redirect('app1:home')

class CrearUsuarioView(CreateView):
    model = User
    template_name = "crearuser.html"
    form_class = CrearUsuario
    success_url = reverse_lazy('app1:Login')

class ConsultaView(CreateView):
    template_name = 'consultas.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('app1:Login')

class TecnicoView(CreateView):
    template_name = 'tecnico.html'
    form_class = TecnicoForm
    success_url = reverse_lazy('app1:index')        

class FacturaView(CreateView):
    template_name = 'factura.html'
    form_class = FacturaForm
    success_url = reverse_lazy('app1:index')     

class ListarClienteView(ListView):
    template_name = 'ListarCliente.html'
    model = Book

    def qet_queryset(self):
        return Cliente.objects.all()

class ListarFacturaView(ListView):
    template_name = 'ListarFactura.html'
    model = Factura

    def qet_queryset(self):
        return Factura.objects.all()

class ListarEmpleadoView(ListView):
    template_name = 'ListarEmpleado.html'
    model = Empleado

    def qet_queryset(self):
        return Empleado.objects.all()

class ListarReparaView(ListView):
    template_name = 'ListarRepara.html'
    model = Repara

    def qet_queryset(self):
        return Repara.objects.all()

class ListarConsultasView(ListView):
    template_name = 'ListarConsultas.html'
    model = Consultas

    def qet_queryset(self):
        return Consultas.objects.all()




