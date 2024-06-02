from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from .utils import get_importance
from .forms import CreateTaskForm, UpdateTaskForm
from .models import Task


@login_required(login_url="users:login")
def my_task(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:register_user')
    
    if request.method == 'POST':
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            data = create_task_form.cleaned_data
            days_left = data['due_date'] - date.today()
            task = Task.objects.create(user=request.user, **data, days_left=days_left.days)
            return redirect(request.path) 
    else:
        create_task_form = CreateTaskForm()

    tasks = request.user.task.all()
    high, middle, low = get_importance(tasks)
    upcoming_tasks = request.user.task.order_by('-due_date')[:5]
    context = {
        'tasks': tasks,
        'create_task_form': create_task_form,
        'H': high,
        'M': middle,
        'L': low,
        'upcoming_tasks': upcoming_tasks
    }

    return render(request, 'index.html', context=context)


def get_task(request, username, task_id) -> HttpResponse:
    if request.user.username != username:
        return redirect('/')
    
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        
        request.POST._mutable = True
        
        if not request.POST['due_date']:
            request.POST['due_date'] = task.due_date
        print(request.POST)
        importance_choice = {'Важно': 'H', 'Средне': 'M', 'Не важно': 'L'}
        request.POST['importance'] = importance_choice[request.POST['importance']]
        # request.POST['days_left'] = request.POST['due_date'] - request.POST['creation_d']
        
        update_form = UpdateTaskForm(request.POST, instance=task)
        if update_form.is_valid():
            update_form.save()
            
        return redirect(request.path)

    update_form = UpdateTaskForm()
    task = Task.objects.filter(id=task_id, user__username=username)[0]
    context = {
        'task': task,
        'update_form': update_form,
        'disable_list': ['creation_d', 'days_left'],
        'min_data': date.today()
    }
    
    return render(request, 'tasks/task.html', context=context)