from enum import unique
from mailbox import NoSuchMailboxError
from tabnanny import verbose
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length = 50)
    camada = models.IntegerField()

    def __str__(self)->str:
        return f'{self.nombre} - {self.camada}'
    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'My Courses'
        ordering = ('nombre', '-camada')
        unique_together = ('nombre', 'camada')

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    profesion = models.CharField(max_length = 50)

class Entregable(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_entrega = models.DateField()
    Entregado = models.BooleanField()