from django.urls import path
from .views import *


app_name = 'tasks'


urlpatterns = [
    path('my_task/', my_task, name='my_task'),
]
