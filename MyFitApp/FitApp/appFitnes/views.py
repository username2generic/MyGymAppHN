from django.shortcuts import render
from .models import Usuarios, Ejercicios, Alimentos
from django.views import generic

# Create your views here.
def index(request):
    numUsuarios = Usuarios.objects.all().count()
    numAlimentos = Alimentos.objects.all().count()
    numEjercicio = Ejercicios.objects.all().count()

    return render(
        request,
        'index.html',
        context=
        {'Usuarios':numUsuarios, 'Alimentos':numAlimentos, 
         'Ejercicios':numEjercicio}
    )

class ListaUsuarios(generic.ListView):
    model = Usuarios