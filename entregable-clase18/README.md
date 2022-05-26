# Ejercicio entregable 6

Crear una web que permite ver los datos de algunos de tus familiares, guardados en una DB

1. deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
2. la clase del modelo deberá guardar mínimo un número, una cadena y una fecha (pueden ser más cosas)
3. se deberán crear como mínimo 3 familiares
4. los familiares se deben ver desde la web

## Pasos

1. crear carpeta
2. `django-admin startproject <nombredelproyecto>` - en este caso mvt6
3. `cd mvt6`
4. `python manage.py migrate`
5. `python manage.py runserver`
6. creamos el archivo `views.py` 
7. TASK: crear una vista. a `views.py` agregamos:

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

9. TASK: pasar parámetros de python a HTML. 

```py
from datetime import datetime

def today(sequest):
    day = datetime.now()

    document = f'hoy es: {day}'

    return HttpResponse(document)
# agregar en mvt6/urls.py la ruta y la llamada a la función
```

10. TASK: parametros desde la url:

```py
# mvt6/views.py
def today(sequest):
    day = datetime.now()

    document = f'hoy es: {day}'

    return HttpResponse(document)
# mvt6/urls.py
...
    path('minombre/<name>/',my_name)
...
```

11. TASK: crear un template:

- crear carpeta **templates**
- crear un archivo html dentro de **templates**
- llamamos a nuestro archivo html desde una nueva vista (en mvt6/views.py)

```py
# mvt6/views.py
from django.template import Template, Context

def template_test(self):
    myfile = open('<pathtofile>/templates/template1.html')

    my_template = Template(myfile.read())

    myfile.close()

    my_context = Context()

    document = my_template.render(my_context)

    return HttpResponse(document)
# mvt6/urls.py
  ...
  path('miprimeraplanilla/', template_test),
  ...
```

12. TASK: variables en planillas

```py
# mvt6/views.py
def vars_template(self):
    name = 'jose'
    last_name = 'aliaga'

    dictionary = {'nombre':name,'apellido':last_name}

    myfile = open('/Users/josemanuelfranciscoaliaga/22/django_portfolio/entregable-clase18/mvt6/mvt6/templates/template1.html')

    my_template = Template(myfile.read())

    myfile.close()

    my_context = Context(dictionary)

    document = my_template.render(my_context)

    return HttpResponse(document)
# mvt6/urls.py
  ...
  path('miaplanillavariable/', vars_template),
  ...
```

```html
# templates/template1.html
  <p style='color: red'>Mi nombre es: {{nombre}}</p>
  <p style='color: green'>Mi apellido es: {{apellido}}</p>
```


























