
from django.urls import path
from app_coder.views import curso, Estudiante, Profesores, cursos, entregables, inicio, lista_curso

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', lista_curso),
    path('cursos/', cursos),
    path('estudiantes/', Estudiante),
    path('profesores/', Profesores),
    path('entregables/', entregables),
    path('', inicio),
]
