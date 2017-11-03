from django import forms
from .models import Empleado,Book,Login,Consultas, Repara, Factura
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DatoForm(forms.ModelForm):

	class Meta:
		model = Empleado
		
		fields = '__all__'

class TecnicoForm(forms.ModelForm):

	class Meta:
		model = Repara
		fields = '__all__'

class AdministradoresForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = '__all__'

class LoginForm(forms.ModelForm):

	class Meta:
		model = Login
		fields = '__all__'

class CrearUsuario(UserCreationForm):
	class Meta:
		 model = User
		 fields= [
            'username',
            'first_name',
            'last_name',
		 ] 
		 labels={
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
		 }

class ConsultaForm(forms.ModelForm):

	class Meta:
		model = Consultas
		fields = '__all__'

class FacturaForm(forms.ModelForm):

	class Meta:
		model = Factura
		fields = '__all__'