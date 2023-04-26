from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=150)
    fecha_nacimiento =models.DateField()
    def _str_(self):
        return self.nombre + ' ' + self.apellido
  
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    def _str_(self):
         return self.nombre 
    
class Usuario(models.Model):
     correo = models.EmailField()
     contrasena = models.CharField(max_length=500)
     def _str_(self) :
          return self.correo
    
class Libro(models.Model):
     titulo = models.CharField(max_length=200)
     sinopsis = models.TextField()
     portada = models.FileField()
     fecha_publicacion = models.DateField('Fecha de publicación')
     num_pag = models.IntegerField('número de páginas', default=0)
     genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
     autores = models.ManyToManyField(Autor)
     calificacion = models.ManyToManyField(Usuario, through='Calificacion')
     def __str__(self):
          return self.titulo
     
class Calificacion(models.Model):
     usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='calificaciones')
     calificacion = models.IntegerField()
     comentario = models.TextField()
     def __str__(self):
          return str(self.calificacion) + '' + self.comentario