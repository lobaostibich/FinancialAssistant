from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(function):
    def wrapper_function(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not Logged in!')
            return redirect('login')
        else:
            return function(request, *args, **kwargs)
    return wrapper_function

def authenticated_user(function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            #TODO colocar mensagem informando que o usuário já está logado
            return redirect('budget')
        else:
            return function(request, *args, **kwargs)
    return wrapper_function



    