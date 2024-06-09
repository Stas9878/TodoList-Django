from django.contrib import admin
from .models import Task, SubTask


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'importance', 'due_date', 'completed')
    readonly_fields = ("creation_date", )

@admin.register(SubTask)
class SubTasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_task', 'due_date', 'completed')
    list_editable = ('parent_task', )
    readonly_fields = ("creation_date",)
    