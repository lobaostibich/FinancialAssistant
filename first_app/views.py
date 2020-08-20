from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'first_app/home.html')

def prices(request):
    return render(request, 'first_app/prices.html')

def money_control(request):
    return render(request, 'first_app/money_control.html')
