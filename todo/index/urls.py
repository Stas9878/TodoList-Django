from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
]