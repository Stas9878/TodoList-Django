from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import get_importance


def my_task(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:register_user')
    
    tasks = request.user.task.all()

    high, middle, low = get_importance(tasks)

    context = {
        'tasks': tasks,
        'H': high,
        'M': middle,
        'L': low
    }

    return render(request, 'index.html', context=context)
