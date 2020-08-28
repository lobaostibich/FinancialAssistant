from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CreateUserForm
from users.decorators import unauthenticated_user, authenticated_user


@authenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("budget")
        else:
            messages.error(request, 'Incorrect Username or Password.')

    return render(request, "users/login.html")

@authenticated_user
def creation_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.cleaned_data.get('username')
            #TODO mostrar mensagem informando que o usuário foi criado com sucesso

            return redirect('login')

    context = {'form':form}
    return render(request, "users/register.html", context)

@unauthenticated_user
def logout_view(request):    
    logout(request)
    #TODO mostrar mensagem avisando que o logout foi bem sucedido

    return redirect('login')
