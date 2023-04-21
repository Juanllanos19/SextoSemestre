from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Libro, Autor, Genero, Usuario, Calificacion

class LibroSerializer(ModelSerializer):
    class Meta:
            model = Libro
            fields = ALL_FIELDS #['id', 'titulo']

class AutorSerializer(ModelSerializer):
      class Meta:
            model = Autor
            fields = ALL_FIELDS #['id', 'titulo']

class GeneroSerializer(ModelSerializer):
      class Meta:
            model = Genero
            fields = ALL_FIELDS #['id', 'titulo']

class UsuarioSerializer(ModelSerializer):
      class Meta:
            model = Usuario
            fields = ALL_FIELDS #['id', 'titulo']

class CalificacionSerializer(ModelSerializer):
      class Meta:
            model = Calificacion
            fields = ALL_FIELDS #['id', 'titulo']