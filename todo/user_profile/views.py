from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .statistics import Statistics
from .forms import UpdateUserForm


@login_required
def user_profile(request, username):
    user = request.user
    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            if 'password' in request.POST:
                user.set_password(request.POST['password'])
            user.save()
            update_session_auth_hash(request, user)
            return redirect(request.path)
    
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
        },
        'form': UpdateUserForm()
    }


    return render(request, 'user_profile/user_profile.html', context=context)
