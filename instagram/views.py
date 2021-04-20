""" Instagram views """
#django
from django.http import HttpResponse
from django.shortcuts import render
#utilities

#models
from users.models import Profile

#forms
from users.forms import SignUpForm
from users.forms import ProfileForm

def hola_mundo(request):
    """
    returns greetings
    """
    now = datetime.now().strftime('%d %B %Y - %H:%M ')
    context = {
        'fecha': now
    }
    return HttpResponse(f' Aqui vamos con otro cursito nojoda!! La mardita fecha del server es {now}')


def say_bye(request, age, name):
    """
    Returns a bye message
    """
    if age >12:
        mensaje = f'Hola {name} te damos la bienvenida a instagram'
    else:
        mensaje = f' Hola {name} no cumples las condiciones para ingresar jodete'
    return HttpResponse (mensaje)


def test(request):
    profile = request.user.profile
    instance = Profile.objects.get(pk=profile.pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()

    else:
        form = ProfileForm(instance=instance)


    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid() :
    #         form.save()
    # else:
    #     form = SignUpForm
    return render(request,'test.html', {'form': form})