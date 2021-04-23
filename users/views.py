"""USERS VIEWS"""
#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse

#models
from .models import Profile
from posts.models import Post
from users.models import User

#forms
from .forms import ProfileForm
from posts.forms import PostForm
from users.forms import SignUpForm


# Views

class UserDetailView(DetailView):
    """Class view for user detail"""
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name='users/detail.html'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

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

        url= reverse('users:detail', kwargs={'username': request.user.username})
        return redirect(url)
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
                return redirect('posts:feed')
            else:
                return render(request, 'users/login.html', {'error': 'invalid username or password'})
    else:
        return redirect('posts:feed')
    return render(request, 'users/login.html')


@login_required
def logout_view (request):
    logout(request)
    # return redirect('login')
    return render(request, 'users/login.html', {'error': 'You logged out succesfully'})


def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return login_view(request)

    else:
        form = SignUpForm
        return render(request,'users/signup.html', {'form' : form })




