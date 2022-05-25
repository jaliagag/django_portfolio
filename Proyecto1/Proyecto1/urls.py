from django.contrib import admin
from django.urls import path
from Proyecto1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('hoy/', dia_de_hoy),
    path('mi_nombre_es/<nombre>', mi_nombre_es),
    path('template-loco/', probandoTemplate),
    path('lafechaes/', lahora),
]

