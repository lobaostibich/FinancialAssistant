from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
#from django.forms import inlineformset_factory
from django.urls import reverse
from django.db.models import Sum

from first_app.models import BudgetControl
from users.forms import BudgetControlForm
from users.decorators import unauthenticated_user


def home(request):
    return render(request, 'first_app/home.html')

@unauthenticated_user
def budget_control(request):
    result = []
    today_month = datetime.today().month
    months = {0: 'JAN',
            1: 'FEB',
            2: 'MAR',
            3: 'APR',
            4: 'MAY',
            5: 'JUN',
            6: 'JUL',
            7: 'AUG',
            8: 'SEP',
            9: 'OCT',
            10: 'NOV',
            11: 'DEC'
    }
    #gets record from the database
    budget_registers = BudgetControl.objects.all()
    #calculates the sum of the goods
    goods_sum = BudgetControl.objects.filter(category='Good').aggregate(Sum('value'))['value__sum']
    #calculates the investments total value
    investments_sum = BudgetControl.objects.filter(category='Investment', month=months[today_month-1]).aggregate(Sum('value'))['value__sum']
    
    #calculates the total profit, total spends and sum for each month
    for month in range(12):
        result.append([0,0,0])
        profits = BudgetControl.objects.filter(category='Profit', month=months[month]).aggregate(Sum('value'))['value__sum']
        spends = BudgetControl.objects.filter(category='Spend', month=months[month]).aggregate(Sum('value'))['value__sum']        
        if profits:
            result[month][0] = int(profits)
        if spends:
            result[month][1] = int(spends)
        result[month][2] = result[month][0]-result[month][1]

    #calculates the annual total spends
    spends_sum = BudgetControl.objects.filter(category='Spend').aggregate(Sum('value'))['value__sum']

    #check if goods_sum is an empty value
    if goods_sum:
        goods_sum = int(goods_sum)
    else:
        goods_sum = 0

    #check if the investments_sum is an empty value
    if investments_sum:
        investments_sum = int(investments_sum)
    else:
        investments_sum = 0

    #check if the spends_sum is an empty value
    if spends_sum:
        spends_sum = int(spends_sum)
    else:
        spends_sum = 0

    return render(request, 'first_app/budget_control.html', {
        'budget_registers':budget_registers,
        'goods_sum':goods_sum,
        'spends_sum':spends_sum,
        'investments_sum':investments_sum,
        'result':result
    })

@unauthenticated_user
def add_record(request):
    #user = request.user.id
    form = BudgetControlForm()
    if request.method == "POST":
        form = BudgetControlForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'first_app/add_records.html', context)

@unauthenticated_user
def update_record(request, pk):
    record = BudgetControl.objects.get(id=pk)
    form = BudgetControlForm(instance=record)
    context = {'form':form}
    if request.method == "POST":
        form = BudgetControlForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return render(request, 'first_app/budget_control.html', context)

    return render(request, 'first_app/add_records.html', context)

@unauthenticated_user
def delete_record(request, pk):
    record = BudgetControl.objects.get(id=pk)
    context = {'item':record}
    if request.method == "POST":
        record.delete()
        return redirect("budget")

    return render(request, "first_app/delete.html", context)