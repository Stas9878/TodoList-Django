from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'users/login.html')
            
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)


def login_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data['username']
            user = get_user_model().objects.filter(Q(username=username) | Q(email=username))[0]
            
            if user:
                login(request, user)
                return redirect('index:index')

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('users:register_user')