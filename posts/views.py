#django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

#Utils
from datetime import datetime

#forms
from posts.forms import PostForm

#models
from posts.models import Post
from users.models import User
from users.models import Profile
# Create your views here.


class PostDetailView(DetailView, LoginRequiredMixin):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'



class PostsFeedView(LoginRequiredMixin, ListView):

    ordering = ('-created')
    context_object_name = 'posts'
    template_name = 'posts/feed.html'
    paginate_by = 100
    model = Post


# @login_required
# def list_posts(request):
#     posts = Post.objects.all().order_by('-created')
#
#
#     return render(request= request,
#                   template_name='posts/feed.html',
#                   context={'posts': posts,
#                            'profile': request.user.profile,
#                            # 'user': request.user
#                     })


@login_required()
def create_post(request):

    user= request.user
    profile = request.user.profile

    if request.method == 'POST':
        instance = Post(user=user, profile=profile)
        form = PostForm( request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('posts:feed')
        else:
            print('error')

    else:

        form = PostForm()

    return render(
        request=request,
        template_name= 'posts/new.html',
        context={ 'form': form,
                  'user': user,
                  'profile': profile,
        }
    )




