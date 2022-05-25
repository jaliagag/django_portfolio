#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cada app tiene sus propios paths

from django.urls import path
from AppCoder.views import profesores, curso
from AppCoder.views import mi_plantilla
#from AppCoder.views import curso, profesores

urlpatterns = [
    path('profesores/', profesores),
    path('curso/', curso),
    path('plantilla/', mi_plantilla),
    #path('appCoder/', include('AppCoder.urls')),
]

