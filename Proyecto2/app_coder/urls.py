
from django.urls import path
from app_coder.views import curso, Estudiante, Profesores, cursos, entregables, inicio, lista_curso

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', lista_curso),
    path('cursos/', cursos,name = "Cursos"),
    path('estudiantes/', Estudiante,name = "Estudiantes"),
    path('profesores/', Profesores,name = "Profesores"),
    path('entregables/', entregables,name = "Entregables"),
    path('', inicio,name = "Inicio"),
]
