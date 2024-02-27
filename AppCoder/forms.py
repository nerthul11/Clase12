from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']

class Form_Curso(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class Form_Estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
   
class Form_Profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
   
class Form_Entregable(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()

class Form_Registro(UserCreationForm):
    username = forms.TextInput()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)