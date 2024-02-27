from django.test import TestCase
from AppCoder.models import Estudiante
from django.urls import reverse
from django.contrib.auth import get_user_model

class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('Inicio')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

class EliminarEstudianteTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(nombre="Juan", apellido="Perez", email="juan@gmail.com")
        user = get_user_model()
        user.objects.create_user('username', password="genericpassword123454321")
    
    def test_setup(self):
        """
        Verificar que creo adecuadamente la instancia de estudiante
        """
        self.assertQuerysetEqual(Estudiante.objects.filter(nombre__icontains="Juan", apellido__icontains="Perez").values(), 
                                 [{'apellido': 'Perez', 'email': 'juan@gmail.com', 'id': 1, 'nombre': 'Juan'}])
    
    def test_login(self):
        """
        Verificar que se inicie sesión
        """
        self.assertTrue(self.client.login(username='username', password='genericpassword123454321'))
    

    def test_eliminar_estudiante(self):
        """
        Verificar que se elimine estudiante al iniciar sesión
        """
        self.client.login(username='username', password='genericpassword123454321')
        url = reverse('Borrar_Estudiante', args=[self.estudiante.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Estudiante.objects.filter(nombre__icontains="Juan", apellido__icontains="Perez"), 
                                 [])

    def test_no_eliminar_estudiante(self):
        """
        Verificar que NO se elimine estudiante sin iniciar sesión
        """
        url = reverse('Borrar_Estudiante', args=[self.estudiante.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Estudiante.objects.filter(nombre__icontains="Juan", apellido__icontains="Perez").values(), 
                                 [{'apellido': 'Perez', 'email': 'juan@gmail.com', 'id': 1, 'nombre': 'Juan'}])