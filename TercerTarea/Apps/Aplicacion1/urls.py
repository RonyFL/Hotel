"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import IndexView, TablaView, BaseView,SomosView, CrearDatoView, AdministradoresView, DatoView, LoginView, ConsultaView, TecnicoView, FacturaView
from .views import ListarClienteView, ListarFacturaView, ListarEmpleadoView, ListarReparaView, ListarConsultasView
from .views import LogoutView, CrearUsuarioView

urlpatterns = [
    
    url(r'^$', LoginView.as_view(),name='home' ),
    url(r'^base$', BaseView.as_view(), name='base' ),
    url(r'^Somos$', SomosView.as_view(), name='Somos' ),
    url(r'^tabla$', TablaView.as_view(),name='tabla'),
    url(r'^Addcrearcliente$', CrearDatoView.as_view(),name='Addcrearcliente'),
    url(r'^index$', IndexView.as_view(),name='index'),
    url(r'^Addcrearadmin$', AdministradoresView.as_view(),name='Addcrearadmin'),
    url(r'^Datos$', DatoView.as_view(),name='Datos'),
    url(r'^Login$', LoginView.as_view(),name='Login'),
    url(r'^SalirUser$', LogoutView,name='logout'),
    url(r'^CrearUser$', CrearUsuarioView.as_view(), name='CreateUser'),
    url(r'^Consulta$', ConsultaView.as_view(), name='Consulta'),
    url(r'^Tecnico$', TecnicoView.as_view(), name='Tecnico'),
    url(r'^Factura$', FacturaView.as_view(), name='Factura'),
    url(r'^ListCliente$', ListarClienteView.as_view(), name='ListCliente'),
    url(r'^ListFactura$', ListarFacturaView.as_view(), name='ListFactura'),
    url(r'^ListEmpleado$', ListarEmpleadoView.as_view(), name='ListEmpleado'),
    url(r'^ListRepara$', ListarReparaView.as_view(), name='ListRepara'),
    url(r'^ListConsulta$', ListarConsultasView.as_view(), name='ListConsulta'),

     
   




    
    
    
 

       
]
