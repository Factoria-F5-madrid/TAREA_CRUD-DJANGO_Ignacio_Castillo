# TAREA_CRUD-DJANGO_Ignacio_Castillo

1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?
   
   El objetivo principal de un CRUD es permitir a los usuarios interactuar (Crear -Create-, Leer -Read-, Modificar -Update- y Borrar -Delete-) con una base de datos de forma sencilla a través de una interfaz web. Google Docs es un ejemplo de aplicación web que usa una estructura de CRUD, ya que permite crear, leer, modificar y borrar un documento.

2. ¿Qué son los patrones de arquitectura en desarrollo de software?
   
   Son soluciones generales y reutilizables para organizar la estructura y los componentes de un sistema de software. No son código específico, sino modelos o guías que ayudan a diseñar aplicaciones robustas,       escalables, mantenibles y que ayudan a separar responsabilidades entre los distintos componentes del sistema.
   - ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?
     Es aquel que separa el software en 3 componentes principales: 1) Modelo	(gestiona los datos, la lógica de negocio, y se comunica con la base de datos), 2) Vista	(muestra la interfaz de usuario. Renderiza       lo que el usuario ve) y 3) Controlador	(recibe las entradas del usuario, las procesa y actualiza el modelo o la vista)
   - ¿Qué es el patrón MVT (Modelo–Vista–Template)?
     Es una variación del MVC.
   - Diferencias entre MVC y MVT.
     La diferencia clave radica en cómo se gestionan la lógica del "controlador" o de la "vista" en cada uno. En MVC, el controlador gestiona tanto el modelo como la vista, mientras que en MVT, la vista gestiona      las solicitudes y respuestas HTTP (de lo cual se encargaba el controlador en MVC) y el template se encarga del renderizado (que es la tarea de la vista en MVC). En suma, en MVC, el controlador es el              "cerebro" que orquesta la interacción entre el modelo y la vista. En MVT, la vista está más involucrada en el manejo de solicitudes y la interacción con el modelo (intuyo que esta variación vino de la mano       de la aparición de las webs dinámicas <los formularios http ya no meramente solicitan un fichero html estático, sino que pueden incluir datos -variables- que influirán en el contenido de la respuesta             http>), mientras que el template se ocupa exclusivamente de la capa de presentación.
   - ¿Cuál de estos dos patrones se usa en Django?
     MVT

3. ¿Cómo se estructura un proyecto en Django?
   
   Un proyecto en Django está dividido en proyecto principal y una o más aplicaciones (apps) dentro de dicho proyecto.
```   
    mi_proyecto/
    │
    ├── manage.py
    ├── mi_proyecto/           # Carpeta del proyecto principal
    │   ├── __init__.py
    │   ├── settings.py        # Configuración general del proyecto
    │   ├── urls.py            # URLs principales del proyecto
    │   └── wsgi.py / asgi.py  # Entrada para servidores web
    │
    ├── mi_app/                # Carpeta de una aplicación (app)
    │   ├── __init__.py
    │   ├── admin.py           # Registro de modelos en el panel de admin
    │   ├── apps.py
    │   ├── models.py          # Modelos: estructura de datos
    │   ├── views.py           # Vistas: lógica que responde a las solicitudes
    │   ├── urls.py            # URLs propias de la app
    │   ├── templates/         # Plantillas HTML
    │   └── migrations/        # Archivos para controlar cambios en la base de datos

```
   - Modelos (models.py)	Definen la estructura de los datos que se guardan en la base de datos. Cada clase representa una tabla.   
   - Vistas (views.py)	Contienen la lógica del servidor: qué hacer con una solicitud y qué respuesta devolver.   
   - Templates (templates/*.html)	Archivos HTML que representan la interfaz visual que ve el usuario. Pueden incluir variables y estructuras de control.   
   - URLs (urls.py)	Conectan las URLs del navegador con las vistas correspondientes. Son el enrutador del proyecto.

   - ¿Para qué se usa el signo “%%” en los templates?
     
     Ejecuta lógica o estructuras de control especificadas entre el primer '%' y el segundo '%' (en un archivo html). Ej/ {% for tarea in tareas %}

4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?
   
   El navegador envía una solicitud POST al servidor con los datos -----> el servidor mapea -busca un match en las rutas de enrutamiento (en urls.py)- para ejecutar la función python correspondiente (en views.py) -----> los cambios generados por esa función se guardan en la base de datos

5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD? ¿para qué es cada una?
   
   - startapp:	Crea una nueva aplicación dentro del proyecto Django
   - runserver:	Inicia el servidor de desarrollo para probar tu proyecto en el navegador
   - makemigrations:	Detecta los cambios en los modelos y crea archivos de migración
   - migrate:	Aplica las migraciones y crea/modifica la base de datos
   - createsuperuser:	Crea un usuario administrador para acceder al panel de administración de Django
   - admin:	Es una herramienta de Django que te permite gestionar modelos (crear, editar, eliminar registros) desde una interfaz web. Solo necesitas registrar tus modelos en admin.py
   - ModelForm:	Es una clase que genera automáticamente un formulario basado en un modelo, facilitando el manejo de formularios en las vistas.

6. ¿Cómo funciona el Admin de Django?
   
   El Admin de Django es una herramienta incorporada que permite gestionar fácilmente el contenido de tu aplicación desde una interfaz web. Funciona como un panel de administración automático donde puedes crear, leer, actualizar y eliminar registros (CRUD) sin necesidad de escribir código adicional. Hay que crear un usuario administrador para poder acceder al panel (python manage.py createsuperuser) y, en el archivo admin.py de la app, registrar los modelos para que se muestren en el panel (admin.site.register(ClassName). SE accede al panel de admin en el navegador (http://localhost:8000/admin)



