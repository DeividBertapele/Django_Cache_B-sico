from django.shortcuts import render
from .models import Usuario
from random import randint

def home(request):
    usuarios = Usuario.objects.all()
    x = randint(1, 20)
    return render(request, 'home.html', {'usuarios': usuarios, 'x': x})