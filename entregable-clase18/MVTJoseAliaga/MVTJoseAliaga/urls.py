from django.contrib import admin
from django.urls import path,include
from MVTJoseAliaga.views import health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('MyFamily/',include('MyFamily.urls')),
]
