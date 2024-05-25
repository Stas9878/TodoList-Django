from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import RegisterForm


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


def login_user(request):
    pass


def logout_user(request):
    pass