from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import get_importance
from .forms import CreateTaskForm
from .models import Task

@login_required(login_url="users:login")
def my_task(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:register_user')
    
    if request.method == 'POST':
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            data = create_task_form.cleaned_data
            
            task = Task.objects.create(user=request.user, **data)
        
    create_task_form = CreateTaskForm()

    tasks = request.user.task.all()
    high, middle, low = get_importance(tasks)
    context = {
        'tasks': tasks,
        'create_task_form': create_task_form,
        'H': high,
        'M': middle,
        'L': low
    }

    return render(request, 'index.html', context=context)

