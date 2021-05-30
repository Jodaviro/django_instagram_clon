"""POSTS VIEWS"""

#django
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
#forms
from posts.forms import PostForm, CommentForm

#models
from posts.models import Post, Comment
# Create your views here.

@login_required
def like_or_dislike_post(request, post, instruction):
    """Like or dislike Posts"""

    current_user= request.user
    post= get_object_or_404(Post, pk=post)

    if instruction =='like':
        post.likes.add(current_user)
    else:
        post.likes.remove(current_user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # return HttpResponse ('<script>history.back();</script>')

class CommentCreateView(LoginRequiredMixin, CreateView):
    """DOEST WORK YETComment Create View"""
    model = Comment
    form_class = CommentForm

    def form_valid(self,form):
        form.instance.user= self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class PostUpdateView(UpdateView, LoginRequiredMixin):
    """Single post view"""
    model = Post
    template_name = 'posts/update_post.html'
    form_class = PostForm

    def get_success_url(self):
        pk = self.object.pk
        return reverse('posts:detail', kwargs={'pk': pk})

class PostDeleteView(DeleteView, LoginRequiredMixin):
    """Delete post view"""
    model = Post

    def get_success_url(self):
        username = self.request.user.username
        return reverse('users:detail', kwargs={'username': username})

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




