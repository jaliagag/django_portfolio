from django.shortcuts import render
from django.http import HttpResponse
from Family.models import *
from django.template import loader


def create_family_member(self,name,last_name,age,birth):

    my_dict = {'name':name,'last_name':last_name,'age':age,'birth':birth}

    my_template = loader.get_template('family_index.html')

    document = my_template.render(my_dict)

    return HttpResponse(document)

def check_family_index(self):

    my_template = loader.get_template('family_index.html')

    document = my_template.render()

    return HttpResponse(document)
