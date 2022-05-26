# Ejercicio entregable 6

Crear una web que permite ver los datos de algunos de tus familiares, guardados en una DB

1. deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
2. la clase del modelo deberá guardar mínimo un número, una cadena y una fecha (pueden ser más cosas)
3. se deberán crear como mínimo 3 familiares
4. los familiares se deben ver desde la web

## Pasos

1. crear carpeta
2. `django-admin startproject <nombredelproyecto>`
3. `cd mvt6`
4. `python manage.py migrate`
5. `python manage.py runserver`
6. creamos el archivo `views.py` 
7. a `views.py` agregamos:

```py
from django.http import HttpResponse

def saludo(request):
  return HttpResponse('Hola django-coder')
```

8. en `mvt6/urls.py` agregamos:

```py
from mvt6.views import saludo
...
    path('saludo/', saludo),
...
```



