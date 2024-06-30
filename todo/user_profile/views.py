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
            'all_tasks': statistics.count_tasks(),
            'count_done_tasks': statistics.count_tasks(completed=True),
            'not_done_tasks': statistics.count_tasks(completed=False),
            'most_subtasks': statistics.most_subtasks(),
            'count_overdue_tasks': statistics.count_overdue_tasks(),
        },
        'subtasks': {
            'all_subtasks': statistics.all_subtasks(),
            'done_subtasks': statistics.all_subtasks(completed=True),
            'not_done_subtasks': statistics.all_subtasks(completed=False),
        }        
    }

    return render(request, 'user_profile/user_profile.html', context=context)
