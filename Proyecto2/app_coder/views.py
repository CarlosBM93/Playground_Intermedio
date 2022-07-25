from django.http import HttpResponse
from django.shortcuts import render

from app_coder.models import Curso

# Create your views here.

def curso(self, nombre, camada):

    curso = Curso(nombre=nombre, camada = camada)
    curso.save()
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>
    """)

def lista_curso(self):
    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})

def inicio(self):
    return render(self, "inicio.html")

def Estudiante(self):
    return render(self,"estudiantes.html")

def Profesores(self):
    return render(self,"profesores.html")

def cursos(self):
    return render(self,"cursos.html")

def entregables(self):
    return render(self,"Entregables.html")