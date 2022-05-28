from django.shortcuts import render
from django.http import HttpResponse

from MyFamily.models import *
from django.template import loader

# >>> yo = Family_member(name='Jose',last_name='Aliaga',age=32,birth='1989-09-02')

def check_family_index(self):

    my_template = loader.get_template('family_index.html')

    document = my_template.render()

    return HttpResponse(document)

def add_members(self,name):
    mydict = { 'name': name }

     

    
