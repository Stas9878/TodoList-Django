from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
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
            password = form.data['password']
            user = get_user_model().objects.filter(Q(username=username) | Q(email=username))
            
            if user.exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index:index')
        return redirect(request.path)

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    logout(request)
    return redirect('users:login_user')