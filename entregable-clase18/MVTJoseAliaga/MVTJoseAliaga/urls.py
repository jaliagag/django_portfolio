from django.contrib import admin
from django.urls import path,include
from MVTJoseAliaga.views import health
#from MyFamily.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('MyFamily/',include('MyFamily.urls')),
#    path('view_family/',check_family_index),
#    path('members/',view_members),
#    path('uncles/',view_uncles),
#    path('cousins/',view_cousins),
#    path('hi/<name>/',hi_family_member),
#    path('add_cousin/<vname>/<vlast_name>/<vage>/<vparents>/<vbirth>/',add_member_cousin),
#    path('add_family_member/<vname>/<vlast_name>/<vage>/<vbirth>/',add_member_family_member),
#    path('add_uncle/<vname>/<vlast_name>/<vage>/<vbirth>/',add_member_uncle),
]
