from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 

from django.http import HttpResponse
from .models import Libros
from .forms import LibroForm

# Create your views here.

def index(request):
   form = UserCreationForm()
   return render(request,'registrarse.html',{'form': form})

def inicio(request):
   return render(request,'paginas/inicio.html')

def nosotros(request):
   return render(request,'paginas/nosotros.html')

def libros(request):
   # Recuperar todos los libros de la base de datos y enviarselos a la vista
   libros = Libros.objects.all()
   return render(request,'libros/index.html',{'libros': libros})

def crear(request):
   formulario = LibroForm(request.POST or None,request.FILES or None)
   if formulario.is_valid():
      formulario.save()
      return redirect('libros')
   return render(request,'libros/crear.html',{'formulario':formulario})

def editar(request,id):
   libro = Libros.objects.get(id=id)
   formulario = LibroForm(request.POST or None,request.FILES or None,instance=libro)
   if formulario.is_valid() and request.method == 'POST':
      formulario.save()
      return redirect('libros')
   return render(request,'libros/editar.html',{'formulario':formulario})

def eliminar(request,id):
   libro = Libros.objects.get(id=id)
   libro.delete()
   return redirect('libros')