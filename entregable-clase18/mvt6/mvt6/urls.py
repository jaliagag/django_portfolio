from django.contrib import admin
from django.urls import path
from mvt6.views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
]
