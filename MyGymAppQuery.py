
from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)

class Alimentos(models.Model):
    alimentosID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=16)
    calorias = models.CharField(max_length=45)
    tamaño_porción = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=16)

class Ejercicios(models.Model):
    ejerciciosID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    categoría = models.CharField(max_length=16)
    gasto_energetico = models.IntegerField()
    repeticiones = models.IntegerField()

class Historial_peso(models.Model):
    historial_peso_ID = models.AutoField(primary_key=True)
    fecha_peso = models.DateField()
    peso = models.FloatField()

class Consumir(models.Model):
    consumirID = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idAlimentos = models.ForeignKey(Alimentos, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    calorias = models.IntegerField()

class Realizar(models.Model):
    realizarID = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idEjercicios = models.ForeignKey(Ejercicios, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    peso = models.FloatField()


python manage.py makemigrations
python manage.py migrate
