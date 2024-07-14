from django.urls import path
from .views import *


app_name = 'tasks'


urlpatterns = [
    path('my_tasks/', my_tasks, name='my_tasks'),
    path('task/<str:username>/<str:task_id>/', get_task, name='get_task'),
    path('delete_task/<str:task_id>/', delete_task, name='delete_task'),
    path('all_subtasks/', all_subtasks, name='all_subtasks'),
    path('task/<str:username>/<str:task_id>/add_subtask/', add_subtask, name='add_subtask'),
    path('delete_subtask/<int:subtask_id>/', delete_subtask, name='delete_subtask'),
]
