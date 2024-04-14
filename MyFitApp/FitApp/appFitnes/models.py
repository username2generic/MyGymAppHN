from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuarioID = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 20)
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length = 7, choices = OPCIONES_ROL, default = 'usuario')

class Alimentos(models.Model):
    alimentoID = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 30)
    porcion = models.IntegerField()
    kcalorias = models.IntegerField()
    usuario = models.ManyToManyField(Usuarios)

class Ejercicios(models.Model):
    ejercicioID = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 30)
    repeticiones = models.IntegerField()
    gasto_energetico = models.IntegerField()
    usuario = models.ManyToManyField(Usuarios)

class HistorialPeso(models.Model):
    ID = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    peso = models.DecimalField(max_digits = 5, decimal_places = 2)
    pesousuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    class Meta:
        ordering= ["-ID"]