#django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Utils
from datetime import datetime

#forms
from posts.forms import PostForm

#models
from posts.models import Post
# Create your views here.


posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
]

@login_required
def list_posts(request):

    # instance = get_object_or_404(Post, pk=request.user.post.pk)
    # post = request.user.post
    #
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES, instance=instance)
    #
    #     if form.is_valid():
    #         form.save()
    #         data = form.cleaned_data
    #
    #
    # else:
    #     form = PostForm(request.user.post )

    return render(request,'posts/feed.html', {'posts': posts})


