from django.db import models

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
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} {self.apellido} | {self.profesion}"
   
class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
