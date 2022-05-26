from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

def create_course(self):
    course = Curso(name='Desarrollo Web', camada='2989')
    course.save()
    document = f'- Curso: {course.name} - camada = {course.camada}'

    return HttpResponse(document)

