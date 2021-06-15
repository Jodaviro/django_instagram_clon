"""POSTS VIEWS"""

#django
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
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
    post = get_object_or_404(Post, pk=post)

    if instruction =='like':
        post.likes.add(current_user)
    else:
        post.likes.remove(current_user)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # return HttpResponse ('<script>history.back();</script>')




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
   

    
    def form_valid(self, form):
        """creates a form instance
         with hidden user and profile values"""
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.pk
        return reverse('posts:detail', kwargs={'pk': pk})





class PostCreateCommentView(PostDetailView, FormMixin ,LoginRequiredMixin):
    """Comment Create View"""
    form_class = CommentForm
    template_name = 'posts/comments.html'

    def get_context_data(self, **kwargs):
        """gets the form in order to be rendered"""
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['comments'] = Comment.objects.filter(post=self.object.pk)
        context['form']= self.form_class
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        """creates a form instance
         with hidden user and profile, and post values"""
        form.instance.post= self.object
        form.instance.user= self.request.user
        form.instance.profile = self.request.user.profile
        

        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse('posts:detail', kwargs={'pk': pk})

    

 
