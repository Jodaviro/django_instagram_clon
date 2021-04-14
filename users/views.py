"""USERS VIEWS"""
#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def login_view(request):
    """login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username or password'})
    return render(request, 'users/login.html')

@login_required
def logout_view (request):
    logout(request)
    # return redirect('login')
    return render(request, 'users/login.html', {'error': 'You logged out succesfully'})