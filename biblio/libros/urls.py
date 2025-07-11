from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),#'' is the root URL, views.lista_libros is the view function to be called, name='lista_libros' is the name of the URL pattern.
    path('<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]