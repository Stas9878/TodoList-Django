from django.urls import path
from .views import *


app_name = 'tasks'


urlpatterns = [
    path('my_task/', my_task, name='my_task'),
    path('task/<str:username>/<str:task_id>/', get_task, name='get_task'),
    path('delete_task/<str:task_id>/', delete_task, name='delete_task'),
    path('task/<str:username>/<str:task_id>/add_subtask/', add_subtask, name='add_subtask'),
]
