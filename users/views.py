"""USERS VIEWS"""
#django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate,login, logout
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import views as auth


#models
from .models import Profile
from posts.models import Post
from users.models import User

#forms
from .forms import ProfileForm
from posts.forms import PostForm
from users.forms import SignUpForm

# Views
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view"""
    model = Profile
    form_class = ProfileForm
    template_name = 'users/update_profile.html'

    def get_object(self, queryset=None):
        """ Return user's profile """
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class UserDetailView(DetailView, LoginRequiredMixin):
    """Class view for user detail"""
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name='users/detail.html'
    model = User
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        """Gets the user profile and its posts"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


# class LoginView(auth.LoginView):
#     """
#     Beatiful simple and abstracted loginview but
#     i cant find the way to give the auth credentials
#     from signupview for automatic login when registration is finished""
#     """
#     template_name = 'users/login.html'
#     redirect_field_name = 'posts:feed'
#     redirect_authenticated_user = True


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
            form = SignUpForm(request.POST)
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm
        return render(request,'users/signup.html', {'form' : form })




