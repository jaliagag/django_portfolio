from django.shortcuts import render
from django.http import HttpResponse

from MyFamily.models import *
from django.template import loader

# >>> yo = Family_member(name='Jose',last_name='Aliaga',age=32,birth='1989-09-02')
my_template = loader.get_template('family_index.html')

def check_family_index(self):

    document = my_template.render()

    return HttpResponse(document)

def add_members(self,name):
    mydict = { 'name': name }

    document = my_template.render(mydict)

    return HttpResponse(document)

     

    
