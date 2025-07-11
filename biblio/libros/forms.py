from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):#A ModelForm is a Django form that automatically generates form fields based on a model. It creates HTML form inputs that correspond to your model's fields.
    class Meta:#Meta is a special inner class in Django that provides configuration options for the outer class. It's not a Python keyword - it's a Django convention.
        model = Libro#This tells Django which model to use for the form 
        fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion', 'isbn'] #This tells Django which fields to include in the form.