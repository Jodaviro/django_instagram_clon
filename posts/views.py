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


postecitos = [
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
    posts = Post.objects.all().order_by('-created')


    return render(request= request,
                  template_name='posts/feed.html',
                  context={'posts': posts,
                           'profile': request.user.profile,
                           # 'user': request.user

                    })


@login_required()
def create_post(request):

    user= request.user
    profile = request.user.profile

    if request.method == 'POST':
        instance = Post(user=user, profile=profile)
        form = PostForm( request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('feed')
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




