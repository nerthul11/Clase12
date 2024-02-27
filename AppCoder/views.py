from django.shortcuts import render
from django.urls import reverse_lazy
from AppCoder import forms, models
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == 'POST':
        formulario = forms.Form_Curso(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = models.Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, 'AppCoder/cursos.html')
    else:
        formulario = forms.Form_Curso()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/cursos.html", contexto)

@login_required
def profesores(request):
      if request.method == "POST":
            formulario = forms.Form_Profesor(request.POST)
            if formulario.is_valid():
                  informacion = formulario.cleaned_data
                  profesor = models.Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                  profesor.save()
                  formulario = forms.Form_Profesor()
                  profesores = models.Profesor.objects.all()
                  contexto= {"profesores": profesores, "formulario": formulario} 
                  return render(request, "AppCoder/profesores.html", contexto)
      else:
            formulario = forms.Form_Profesor()
            profesores = models.Profesor.objects.all()
            contexto= {"profesores": profesores, "formulario": formulario} 
      return render(request, "AppCoder/profesores.html", contexto)


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def buscar(request):
  if request.GET['camada']:
    camada = request.GET['camada']
    cursos = models.Curso.objects.filter(camada__icontains=camada)
    return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})
  else:
    respuesta = 'No enviaste datos'
  
  return render(request, 'AppCoder/inicio.html', {'respuesta': respuesta})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)            
            return render(request, "AppCoder/inicio.html", {"mensaje": f'Bienvenido {user.username}'})         
    else:
        form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})

# Vista de registro
def register(request):
      if request.method == 'POST':
            form = forms.Form_Registro(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            form = forms.Form_Registro()     
      return render(request,"AppCoder/register.html" ,  {"form":form})

# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "AppCoder/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppCoder/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')

# List views
class CursoListView(ListView):
    model = models.Curso
    context_object_name = "cursos"
    template_name = "AppCoder/curso_lista.html"

class CursoDetailView(DetailView):
    model = models.Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreateView(CreateView):
    model = models.Curso
    template_name = "AppCoder/curso_crear.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada']
    
class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Curso
    template_name = "AppCoder/curso_editar.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada']
    
class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Curso
    template_name = "AppCoder/curso_borrar.html"
    success_url = reverse_lazy('ListaCursos')

# Create
class Crear_Estudiante(CreateView):
    model = models.Estudiante
    template_name = "AppCoder/estudiante_crear.html"
    success_url = reverse_lazy('Lista_Estudiantes')
    fields = ['nombre', 'apellido', 'email']

# Read
class Listar_Estudiantes(ListView):
    model = models.Estudiante
    context_object_name = "estudiantes"
    template_name = "AppCoder/estudiantes_lista.html"
    
class Detallar_Estudiante(DetailView):
    model = models.Estudiante
    template_name = "AppCoder/estudiantes_detalle.html"

# Update
class Editar_Estudiante(LoginRequiredMixin, UpdateView):
    model = models.Estudiante
    template_name = "AppCoder/estudiantes_editar.html"
    success_url = reverse_lazy('Lista_Estudiantes')
    fields = ['nombre', 'apellido', 'email']

# Delete
class Borrar_Estudiante(LoginRequiredMixin, DeleteView):
    model = models.Estudiante
    template_name = "AppCoder/estudiantes_borrar.html"
    success_url = reverse_lazy('Lista_Estudiantes')