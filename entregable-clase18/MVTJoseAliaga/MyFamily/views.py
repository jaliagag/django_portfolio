from django.shortcuts import render
from django.http import HttpResponse

from MyFamily.models import *
from django.template import loader

my_template = loader.get_template('family_index.html')

def check_family_index(self):

    document = my_template.render()

    return HttpResponse(document)

def hi_family_member(self,name):
    mydict = { 'name': name }

    document = my_template.render(mydict)

    return HttpResponse(document)

def add_member_cousin(self,vname,vlast_name,vage,vparents,vbirth):

    checking = 'Primos'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'parents':vparents,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Cousin(name=vname,last_name=vlast_name,age=vage,parents=vparents,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)

def add_member_family_member(self,vname,vlast_name,vage,vbirth):

    checking = 'Miembros de familia directa'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Family_member(name=vname,last_name=vlast_name,age=vage,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)

def add_member_uncle(self,vname,vlast_name,vage,vbirth):

    checking = 'Tíos'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Uncle(name=vname,last_name=vlast_name,age=vage,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)
