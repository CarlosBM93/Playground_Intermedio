from django.contrib import admin

from app_coder.models import Curso, Entregable, Profesor, Estudiante

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)