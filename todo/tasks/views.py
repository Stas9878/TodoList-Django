from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from datetime import date, datetime
from .utils import get_importance
from .forms import CreateTaskForm, UpdateTaskForm, CreateSubTaskForm
from .models import Task, SubTask


@login_required
def my_tasks(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:login_user')
    
    if request.method == 'POST':
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            data = create_task_form.cleaned_data
            days_left = data['due_date'] - date.today()
            Task.objects.create(user=request.user, **data, days_left=days_left.days)
        return redirect(request.path) 
    else:
        create_task_form = CreateTaskForm()

    tasks = request.user.task.all()

    for i in range(len(tasks)):
        tasks[i].days_left = (tasks[i].due_date - date.today()).days
        tasks[i].save()
    
    high, middle, low = get_importance(tasks)
    upcoming_tasks = request.user.task.filter(days_left__gte=0).order_by('-due_date')[:5]

    context = {
        'tasks': tasks,
        'create_task_form': create_task_form,
        'H': high,
        'M': middle,
        'L': low,
        'upcoming_tasks': upcoming_tasks,
    }

    return render(request, 'index.html', context=context)


@login_required
def get_task(request, username, task_id) -> HttpResponse:
    if request.user.username != username:
        return redirect('/')
    
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        
        request.POST._mutable = True

        if not request.POST['due_date']:
            request.POST['due_date'] = task.due_date
        else:
            request.POST['due_date'] = datetime.strptime(request.POST['due_date'], '%Y-%m-%d')

        request.POST['importance'] = request.POST['importance']
        request.POST['days_left'] = (request.POST['due_date'].date() - date.today()).days
        request.POST['creation_d'] = task.creation_date
        
        update_form = UpdateTaskForm(request.POST, instance=task)

        if update_form.is_valid():
            update_form.save()
            
        return redirect(request.path)

    update_form = UpdateTaskForm()
    
    task = Task.objects.filter(id=task_id, user__username=username)[0]
    subtasks = task.subtask_set.all()

    context = {
        'task': task,
        'update_form': update_form,
        'disable_list': ['creation_d', 'days_left'],
        'due_date': task.due_date.strftime(format='%Y-%m-%d'),
        'subtasks': subtasks,
    }
    
    return render(request, 'tasks/task.html', context=context)


@login_required
def delete_task(request, task_id) -> HttpResponseRedirect:
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')


@login_required
def search_tasks(request):
    search_query = request.GET.get('search_field')
    if search_query:
        tasks = Task.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query),
            user=request.user
        )
    else:
        tasks = Task.objects.filter(user=request.user)

    context = {
        'tasks': tasks.order_by('-creation_date', 'title')
    }

    return render(request, 'tasks/search/search_tasks.html', context)


@login_required
def all_tasks(request):    
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/all_tasks.html', context=context)


@login_required
def all_subtasks(request):
    subtasks = SubTask.objects.filter(parent_task__user=request.user)
    context = {
        'subtasks': subtasks.order_by('-creation_date', 'parent_task__title')
    }
    return render(request, 'tasks/all_subtasks.html', context=context)

@login_required()
def add_subtask(request, username, task_id) -> HttpResponseRedirect | HttpResponse:
    if request.user.username != username:
        return redirect('/')
    
    if request.method == 'POST':
        form = CreateSubTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            SubTask.objects.create(
                parent_task=data['parent_task'], 
                title=data['title'],
                description=data['description'],
            )
        
        return redirect(
            'tasks:get_task', 
            username=username,
            task_id=task_id
        )

    form = CreateSubTaskForm()
    
    user_tasks = Task.objects.filter(user=request.user)
    context = {
        'form': form,
        'user_tasks': user_tasks,
        'task_id': int(task_id)
    }

    return render(request, 'tasks/add_subtask.html', context=context)


@login_required
def delete_subtask(request, subtask_id) -> HttpResponseRedirect:
    subtask = SubTask.objects.get(id=subtask_id)
    subtask.delete()
    return redirect(request.META.get('HTTP_REFERER'))
