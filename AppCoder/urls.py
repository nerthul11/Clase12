"""
URL configuration for Clase10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html', ), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('cambiarClave', views.CambiarClave.as_view(), name="CambiarClave"),
    path('buscar', views.buscar, name="Buscar"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursos/lista', views.CursoListView.as_view(), name="ListaCursos"),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name="NuevoCurso"),
    path('cursos/<pk>', views.CursoDetailView.as_view(), name="DetalleCurso"),
    path('cursos/<pk>/editar', views.CursoUpdateView.as_view(), name="EditarCurso"),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name="BorrarCurso"),
    path('estudiantes', views.Listar_Estudiantes.as_view(), name="Lista_Estudiantes"),
    path('estudiantes/nuevo', views.Crear_Estudiante.as_view(), name="Nuevo_Estudiante"),
    path('estudiantes/<pk>', views.Detallar_Estudiante.as_view(), name="Detalle_Estudiante"),
    path('estudiantes/<pk>/editar', views.Editar_Estudiante.as_view(), name="Editar_Estudiante"),
    path('estudiantes/<pk>/borrar', views.Borrar_Estudiante.as_view(), name="Borrar_Estudiante"),
]