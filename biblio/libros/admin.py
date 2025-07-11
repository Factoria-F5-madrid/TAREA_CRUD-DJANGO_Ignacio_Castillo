from django.contrib import admin

# Register your models here.
from .models import Libro

@admin.register(Libro) #This decorator registers the Libro model with the Django admin, It's equivalent to admin.site.register(Libro, LibroAdmin)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn') #This is a tuple of field names that will be displayed in the admin interface
    search_fields = ('titulo', 'autor', 'isbn') #This is a tuple of field names that will be used to search for books in the admin interface
    list_filter = ('fecha_publicacion',) #This is a tuple of field names that will be used to filter the books in the admin interface