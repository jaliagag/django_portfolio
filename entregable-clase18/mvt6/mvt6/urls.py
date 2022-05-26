from django.contrib import admin
from django.urls import path
from mvt6.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('dia/', today),
    path('minombre/<name>/',my_name),
    path('miprimeraplanilla/', template_test),
    path('miaplanillavariable/', vars_template),
]
