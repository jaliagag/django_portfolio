#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import loader

def health(request):
  return HttpResponse('Status 200 - OK')

def family_index(self):
    name = 'jose'
    last_name = 'aliaga'

    my_dict = {'name':name,'last_name':last_name}

    my_template = loader.get_template('family_index.html')

    document = my_template.render(my_dict)

    return HttpResponse(document)

