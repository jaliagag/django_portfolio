# Instrucciones

## Requisitos

- python3
- django
- git

## Configuración 

```console
git clone https://github.com/jaliagag/django_portfolio.git
cd django_portfolio
git pull origin entregable-clase18
cd entregable-clase18/MVTJoseAliaga
python manage.py runserver
```

## Uso/URLs

Usar **localhost:8000/** más uno de estos endpoints:

- `health/` --> comprobar que el server está corriendo adecuadamente. Deberíamos ver `Status 200 - OK`
- `MyFamily/` --> nos muestra el template
- `MyFamily/members/` --> nos muestra los miembros de la tabla `MyFamily_family_member`
- `MyFamily/uncles/` --> nos muestra los miembros de la tabla `MyFamily_uncle`
- `MyFamily/cousins/` --> nos muestra los miembros de la tabla `MyFamily_cousin`
- `MyFamily/fixed/` --> añade 3 miembros de manera fija y nos los muestra en la web
- `MyFamily/hi/<name>/` --> nos saluda
- `MyFamily/add_cousin/<vname>/<vlast_name>/<vage>/<vparents>/<vbirth>/` --> agregar un primo a la base de datos
- `MyFamily/add_family_member/<vname>/<vlast_name>/<vage>/<vbirth>/` --> agregar un miembro de familia directa a la base de datos
- `MyFamily/add_uncle/<vname>/<vlast_name>/<vage>/<vbirth>/` --> agregar un tío a la base de datos

## Ejemplos de la db

![001](./img/001.png)

![002](./img/002.png)

![003](./img/003.png)

- agregamos un miembro de ejemplo

![004](./img/004.png)

![005](./img/005.png)


