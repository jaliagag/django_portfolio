#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

# TASK: crear una vista
def saludo(request):
  return HttpResponse('Hola django-coder')

# TASK: pasar parámetros de python a HTML
def today(sequest):
    day = datetime.now()

    document = f'hoy es: {day}'

    return HttpResponse(document)

# TASK: pasar parámetros desde la url

def my_name(self, name):
    document = f'mi nombre es {name}'

    return HttpResponse(document)

# TASK: crear (y usar) un template

def template_test(self):
    myfile = open('/Users/josemanuelfranciscoaliaga/22/django_portfolio/entregable-clase18/mvt6/mvt6/templates/template1.html')

    my_template = Template(myfile.read())

    myfile.close()

    my_context = Context()

    document = my_template.render(my_context)

    return HttpResponse(document)

# TASK: pasar variables al template

def vars_template(self):
    name = 'jose'
    last_name = 'aliaga'

    # TASK: variables complejas en plantillas

    my_list = [2,3,4,5,6,1]

    dictionary = {'nombre':name,'apellido':last_name,'lista':my_list}

    myfile = open('/Users/josemanuelfranciscoaliaga/22/django_portfolio/entregable-clase18/mvt6/mvt6/templates/template1.html')

    my_template = Template(myfile.read())

    myfile.close()

    my_context = Context(dictionary)

    document = my_template.render(my_context)

    return HttpResponse(document)

def using_loader(self):
    name = 'jose'
    last_name = 'aliaga'
    dt = datetime.now()

    my_list = [2,3,4,5,6,1]

    dictionary = {'nombre':name,'apellido':last_name,'hoy':dt,'lista':my_list}

    my_template = loader.get_template('template1.html')

    document = my_template.render(dictionary) # ya no necesitamos un contexto

    return HttpResponse(document)




