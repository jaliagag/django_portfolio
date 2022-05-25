#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Template, Context
from django.template import  loader
from datetime import datetime,timedelta

# funciones de la view

def saludo(request):
    return HttpResponse('Hola mundo')

def segunda_vista(request):
    return HttpResponse('<h1>Hola mundo</h1>')

def dia_de_hoy(request):
    dia = datetime.datetime.now()

    texto = f'hoy es día: <br>', dia

    return HttpResponse(texto)

def mi_nombre_es(self,nombre):
    texto = f'mi nombre es: ', nombre

    return HttpResponse(texto)

def probandoTemplate(self):
    nom = 'jose'
    ap = 'ali'
    listaDeNotas=[2,5,7,3]

    diccionario = {'nombre':nom,'apellido':ap, 'listanotas':listaDeNotas}

    #miHtml=open('template.html')
    #plantilla = Template(miHtml.read()) # se carga en memorio nuestro documento, template1
    #miHtml.close()

    #miContexto = Context(diccionario) # permitimos que html use las variables 
    #miContexto = Context()
    plantilla = loader.get_template('template.html')

    #documento = plantilla.render(miContexto)
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def lahora(self):
  dt = datetime.now()
  diccionario = {'ledt':dt}
  miHtml = open('/Users/josemanuelfranciscoaliaga/22/22_coderhouse_python_jaliaga/clase18/Proyecto1/Plantillas/dateme.html')
  plantilla = Template(miHtml.read())

  miHtml.close()

  miContexto = Context(diccionario)

  ledt = plantilla.render(miContexto)

  return HttpResponse(ledt)
