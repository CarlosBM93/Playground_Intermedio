
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.forms import Cursoformulario

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

"""def cursoFormulario(request):

    if request.method =='POST':
        curso = Curso(nombre = request.POST['curso'], camada = request.POST['camada'])
        curso.save()
        
        return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/cursoFormulario.html")
"""

def cursoFormulario(request):

    print('method: ', request.method)
    print('post: ', request.POST)

    if request.method =='POST':

        miFormulario = Cursoformulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            curso = Curso(nombre = data['curso'], camada = data['camada'])
            curso.save()
            return render(request, "inicio.html")

    else:
        miFormulario = Cursoformulario()

    return render(request, "cursoFormulario.html",{"miFormulario" : miFormulario})

def busquedaCamada(request):

    return render(request, 'busquedaCamada.html')

def buscar(request):

    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "resultadoBusqueda.html",{"cursos":cursos, "camada" : camada})
    
    else:

        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

