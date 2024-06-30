from tasks.models import Task, SubTask
from django.db.models import Count, Max


class Statistics:
    def __init__(self, user):
        self.user = user
    

    def count_tasks(self, **kwargs) -> int:
        return Task.objects.filter(user=self.user, **kwargs).count()
    
    
    def count_overdue_tasks(self) -> int:
        return Task.objects.filter(user=self.user, days_left__lt=0).count()
    

    def all_subtasks(self, **kwargs):
        return SubTask.objects.filter(parent_task__user=self.user, **kwargs).count()


    def most_subtasks(self) -> int:
        max_sub = Task.objects.filter(user=self.user).values('pk', 'title').annotate(
            subtasks=Count('subtask')
        ).order_by('subtasks').last()
        return max_sub
    