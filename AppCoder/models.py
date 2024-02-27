from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
   
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    profesion = models.CharField(null=True, max_length=30)
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} {self.apellido} | {self.profesion}"
   
class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"