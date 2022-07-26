from django.contrib import admin
from django.urls import path
from app_coder.views import curso, Estudiante, Profesores, cursos, entregables, inicio, lista_curso, cursoFormulario, busquedaCamada, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = "Inicio"),
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', lista_curso),
    path('cursos/', cursos, name = "Cursos"),
    path('estudiantes/', Estudiante, name = "Estudiantes"),
    path('profesores/', Profesores, name = "Profesores"),
    path('entregables/', entregables, name = "Entregables"),
    path('cursoFormulario/', cursoFormulario , name = "cursoFormulario"),
    path('busquedaCamada/', busquedaCamada , name = "BusquedaCamada"),
    path('buscar/', buscar , name = "buscar"),
]
