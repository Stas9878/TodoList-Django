from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request, username):
    if not request.user.is_authenticated:
        return redirect('users:register_user')
    
    return render(request, 'user_profile/user_profile.html')
