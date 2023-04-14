from django.contrib import admin
from .models import Autor, Genero, Usuario, Libro, Calificacion
# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Calificacion)