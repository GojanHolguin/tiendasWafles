from django.db import models

# Create your models here.


class Categorias_w(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Productos_w(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias_w, on_delete=models.PROTECT)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


class Users(models.Model):
    nombreUsuario = models.CharField(max_length=250)
    nombres = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    password1 = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreUsuario
