from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    IMPORTANCE_CHOICES = {
        ('H', 'Важно'),
        ('M', 'Средне'),
        ('L', 'Не важно'),
    }

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(get_user_model(), related_name='task', on_delete=models.CASCADE, default=None)
    importance = models.CharField(max_length=1,
                  choices=IMPORTANCE_CHOICES,
                  default="L")
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    days_left = models.IntegerField(blank=True, null=False, default=1)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title[:30]}'
    

class SubTask(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'SubTask({self.title[:30]}) for Task({self.parent_task.title[:30]})'