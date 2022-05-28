from django.shortcuts import render
from django.http import HttpResponse

from Family.models import *
from django.template import loader

#def create_family_member(self,name,last_name,age,birth):
def create_family_member(self,name,last_name,age):

    #new_member = Family_member(name=name,last_name=last_name,age=age,birth=birth)
    new_member = Family_member(name=name,last_name=last_name,age=age)
    new_member.save()

#    my_dict = {'name':name,'last_name':last_name,'age':age,'birth':birth}
#
#    my_template = loader.get_template('family_index.html')
#
#    document = my_template.render(my_dict)

    document = f'Nuevo miembro agregado con éxito! <br>- Nombre: {new_member.name}<br>- Apellido: {new_member.last_name}<br>- Edad: {new_member.age}<br>- Fecha de nacimiento: {new_member.birth}'
    return HttpResponse(document)

def check_family_index(self):

    my_template = loader.get_template('family_index.html')

    document = my_template.render()

    return HttpResponse(document)
