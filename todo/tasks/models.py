from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    assigned_to = models.ManyToManyField(get_user_model())
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)


class SubTask(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    assigned_to = models.ManyToManyField(get_user_model())
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)