from django.urls import path

from MyFamily import views

urlpatterns = [
    path('',views.check_family_index),
    path('members/',views.view_members),
    path('uncles/',views.view_uncles),
    path('cousins/',views.view_cousins),
    path('hi/<name>/',views.hi_family_member),
    path('add_cousin/<vname>/<vlast_name>/<vage>/<vparents>/<vbirth>/',views.add_member_cousin),
    path('add_family_member/<vname>/<vlast_name>/<vage>/<vbirth>/',views.add_member_family_member),
    path('add_uncle/<vname>/<vlast_name>/<vage>/<vbirth>/',views.add_member_uncle),
    path('fixed/',views.fixed_members),
]
