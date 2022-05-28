from django.contrib import admin
from django.urls import path
from MVTJoseAliaga.views import health
from MyFamily.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('view_family/',check_family_index),
    path('holis/<name>/',add_members),
]
