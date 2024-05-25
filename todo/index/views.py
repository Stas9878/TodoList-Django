from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('users:register_user')

    