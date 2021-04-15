"""USERS VIEWS"""
#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

#models
from .models import Profile
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


def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']
        first_name = request.POST['first_name']

        #password validation
        if password == password_confirm:


            #username validation
            # Search if the username already exist in the database
            db_username = User.objects.filter(username=username)
            if db_username :
                error = 'Username already registered'
                return render(request, 'users/signup.html', {'error': error})

            #email validation
            # defaul value for empty email field is '', so we need to filter default value
            if email !='' :
                # Search if the email already exist in the database
                db_email = User.objects.filter(email=email)
                if db_email :
                    error = 'Email already registered with other username'
                    return render(request, 'users/signup.html', {'error': error})

            #User creation
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name
            )
            #Profile creation
            profile = Profile(user=user)
            profile.save()
            return login_view(request)

        else:
            error = "Password fields didn't match"
            return render(request,'users/signup.html', { 'error': error})

    return render(request,'users/signup.html')


def update_profile(request):
    pass
    return render(request, 'users/update_profile.html')
