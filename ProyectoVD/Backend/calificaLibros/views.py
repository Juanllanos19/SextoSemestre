from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Libro, Autor, Genero, Usuario, Calificacion
from .serializers import LibroSerializer, AutorSerializer, GeneroSerializer, UsuarioSerializer, CalificacionSerializer, LibrosGetSerializer

class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    #serializer_class = LibroSerializer
    def get_serializer(self):
        if self.request.method in ['GET']:
            return LibrosGetSerializer
        return LibroSerializer

class AutoresViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class GenerosViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CalificacionesViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
