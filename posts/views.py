"""POSTS VIEWS"""

#django
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#forms
from posts.forms import PostForm

#models
from posts.models import Post
# Create your views here.


class PostDetailView(DetailView, LoginRequiredMixin):
    """Single post view"""
    model = Post
    context_object_name = 'post'
    template_name = 'posts/detail.html'

class PostsFeedView(LoginRequiredMixin, ListView):
    """Views that list all posts"""
    ordering = ('-created')
    context_object_name = 'posts'
    template_name = 'posts/feed.html'
    paginate_by = 100
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    """View for a new post creation"""
    model = Post
    form_class = PostForm
    template_name = 'posts/new.html'
    context_object_name = 'form'
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        """creates a form instance
         with hidden user and profile values"""
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)




