from django.contrib import admin
from .models import Task, SubTask


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'importance','creation_date', 'due_date', 'completed']


@admin.register(SubTask)
class SubTasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent_task', 'creation_date', 'due_date', 'completed']
    list_editable = ['parent_task']
