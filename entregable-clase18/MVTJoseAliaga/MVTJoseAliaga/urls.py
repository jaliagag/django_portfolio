from django.contrib import admin
from django.urls import path
from MVTJoseAliaga.views import health
from MyFamily.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('view_family/',check_family_index),
    path('holis/<name>/',hi_family_member),
    path('add_cousin/<vname>/<vlast_name>/<vage>/<vparents>/<vbirth>/',add_member_cousin),
    path('add_family_member/<vname>/<vlast_name>/<vage>/<vbirth>/',add_member_family_member),
    path('add_uncle/<vname>/<vlast_name>/<vage>/<vbirth>/',add_member_uncle),
]
