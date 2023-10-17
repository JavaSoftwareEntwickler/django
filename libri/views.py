from django.shortcuts import render
from .models import Libro

# Create your views here.
def libri(request):
    libri = Libro.objects.all()
    return render(request, 'libri.html',{'libri':libri})

# Create your views here.
def home(request):
    libri = Libro.objects.all()
    return render(request, 'home.html',{'libri':libri})

# Create your views here.
def prova(request):
    libri = Libro.objects.all()
    return render(request, 'base.html',{'libri':libri})

# Create your views here.
def acquista(request):
    libri = Libro.objects.all()
    return render(request, 'acquista.html',{'libri':libri})

