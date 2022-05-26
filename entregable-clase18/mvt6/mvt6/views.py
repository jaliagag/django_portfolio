#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse


def saludo(request):
  return HttpResponse('Hola django-coder')
