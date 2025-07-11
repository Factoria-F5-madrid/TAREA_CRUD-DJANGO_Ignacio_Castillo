from django.shortcuts import render

# Create your views here.
from django.shortcuts import  get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()#This is a Django ORM query to get all the books from the database
    return render(request, 'libros/lista_libros.html', {'libros': libros})#2nd arg is Template path (looks in templates/libros/) and 3rd arg is context (a dictionary of variables to be used in the template. here mapping libros -retrieved from the database- to the template's libros variable)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)#This is a Django ORM query to get a single book from the database. 1st arg is the model -also a table in database- to query, 2nd arg is the primary key of the book to get. If the book is not found, it raises a 404 error.
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)#This creates a form instance with the data submitted in the POST request.
        if form.is_valid():
            form.save()#This saves the form data to the database.
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})