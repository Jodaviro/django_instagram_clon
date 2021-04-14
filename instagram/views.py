""" Instagram views """
#django
from django.http import HttpResponse
from django.shortcuts import render
#utilities
from datetime import datetime

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