"""USERS VIEWS"""
#django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate,login, logout
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth import views as auth
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

#models
from .models import Profile, Contact
from posts.models import Post
from users.models import User


#forms
from .forms import ProfileForm
from posts.forms import PostForm
from users.forms import SignUpForm

# Views


class FollowersView(LoginRequiredMixin, DetailView):
    """Followers View"""
    model = User
    template_name = 'users/followers.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'users'

class FollowingView(LoginRequiredMixin, DetailView):
    """Following view"""
    model = User
    template_name = 'users/following.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'users'

class FollowOrUnforllowView(UpdateView, LoginRequiredMixin):
    """ does't work yet
    trying to transform de follow_or_unfollow in a class view"""
    slug_field = 'username'
    slug_url_kwarg = 'username'

@login_required
def follow_or_unfollow(request, profile, instruction):
    """Follow or unfollow view"""
    current_profile = request.user.profile
    another_profile = get_object_or_404(Profile, pk=profile)

    if instruction == "add":
        """
        follows another_profile is instruccion == 'add' 
        otherwhise unfollows
        """
        Contact.follow(current_profile,another_profile)
    else:
        Contact.unfollow(current_profile,another_profile)


    return HttpResponseRedirect(request.META['HTTP_REFERER'])


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
    context_object_name = 'users'


    def get_context_data(self, **kwargs):
        """Gets the user profile and its posts"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth.LoginView):
    """ Login View"""
    template_name = 'users/login.html'
    redirect_field_name = 'posts:feed'
    redirect_authenticated_user = True


@login_required
def logout_view (request):
    logout(request)
    return render(request, 'users/login.html', {'error': 'You logged out succesfully'})


class SignUpView(FormView):
    """Signup View"""
    template_name = 'users/signup.html'
    success_url = 'posts:feed'
    form_class = SignUpForm

    def form_valid(self, form):
        # save the new user
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.get_success_url())
