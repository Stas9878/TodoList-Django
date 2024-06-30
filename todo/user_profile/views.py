from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .statistics import Statistics


@login_required
def user_profile(request, username):
    user = request.user
    if not user.is_authenticated:
        return redirect('users:register_user')
    
    statistics = Statistics(user)
    context = {
        'tasks': {
            'all_tasks': (
                'Всего задач: ', 
                statistics.count_tasks()
            ),
            'count_done_tasks': (
                'Выполненных: ',
                statistics.count_tasks(completed=True)
            ),
            'not_done_tasks': (
                'Ожидающих выполнения: ', 
                statistics.count_tasks(completed=False)
            ),
            'count_overdue_tasks': (
                'Просроченных:',
                statistics.count_overdue_tasks()
            ),
            'most_subtasks': (
                'С самым большим числом подзадач: ', 
                statistics.most_subtasks()
            ),
        },
        'subtasks': {
            'all_subtasks': (
                'Всего подзадач: ',
                statistics.all_subtasks()
            ),
            'done_subtasks': (
                'Выполненных:', 
                statistics.all_subtasks(completed=True)
            ),
            'not_done_subtasks': (
                'Невыполненных: ', 
                statistics.all_subtasks(completed=False)
            ),
        }        
    }

    return render(request, 'user_profile/user_profile.html', context=context)
