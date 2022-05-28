from django.contrib import admin
from django.urls import path
from MVTJoseAliaga.views import health
from Family.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('nuevo/<name>/<last_name>/<age>/',create_family_member),
    path('view_family/',check_family_index),
]
