#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre='asd',camada=10293)
    curso.save()
    document = f'curso: {curso.nombre} - camada: {curso.camada}'

    return HttpResponse(document)


def profesores(self):
    #curso = Curso(nombre='asd',camada=10293)
    #curso.save()
    document = f'Pagina pa profes'

    return HttpResponse(document)
