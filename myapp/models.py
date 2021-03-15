from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    class Meta: 
        verbose_name_plural = "Autores"
    def __str__(self):
        cadena = self.apellido + ", "+self.nombre
        return cadena
    
class Libro(models.Model):
    titulo = models.CharField(max_length=128)
    editorial = models.CharField(max_length=128)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    class Meta: 
        verbose_name_plural = "Libros"
    def __str__(self):
        cadena = self.titulo+"("+self.autor.apellido+")"
        return cadena
