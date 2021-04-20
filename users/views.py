"""USERS VIEWS"""
#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

#models
from .models import Profile
from posts.models import Post

#forms
from .forms import ProfileForm
from posts.forms import PostForm
from users.forms import SignUpForm


# Views

@login_required
def update_profile(request):
    """Profile view"""
    profile = request.user.profile
    #makes a query in the database.
    instance = get_object_or_404(Profile, pk=profile.pk)

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()

        return redirect('update_profile')
    else:
        form = ProfileForm(instance=instance)

    return render(
        request = request,
        template_name= 'users/update_profile.html',
        context = {'form': form,
                   'user': request.user,
                   'profile': profile
        }
    )


def login_view(request):
    """login view"""
    if request.user.is_anonymous:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                return render(request, 'users/login.html', {'error': 'invalid username or password'})
    else:
        return redirect('feed')
    return render(request, 'users/login.html')


@login_required
def logout_view (request):
    logout(request)
    # return redirect('login')
    return render(request, 'users/login.html', {'error': 'You logged out succesfully'})


def signup_view(request):
    """Sign up view"""
    form = SignUpForm
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
                # Check if  email already exist in the database
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
            profile = Profile(user=user, website='', biography ='', phone_number= '')
            profile.save()
            return login_view(request)

        else:
            error = "Password fields didn't match"
            return render(request,'users/signup.html', { 'error': error})

    return render(request,'users/signup.html', {'form' : form })




