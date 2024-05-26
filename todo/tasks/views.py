from django.http import HttpResponse
from django.shortcuts import render, redirect


def my_task(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:register_user')
    
    return render(request, 'index.html')
