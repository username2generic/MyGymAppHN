from django.contrib import admin
from .models import Usuarios, Alimentos, Ejercicios

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Alimentos)
admin.site.register(Ejercicios)