#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cada app tiene sus propios paths

from django.urls import path
from AppCoder import views
#from AppCoder.views import curso, profesores

urlpatterns = [
    path('profesores/', views.profesores),
    path('curso/', views.curso),
    #path('appCoder/', include('AppCoder.urls')),
]

