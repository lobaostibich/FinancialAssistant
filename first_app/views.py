from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
#from django.forms import inlineformset_factory
from django.db.models import Sum

from first_app.models import BudgetControl, FixedValues
from users.forms import BudgetControlForm, FixedValuesForm
from django.forms import inlineformset_factory
from users.decorators import unauthenticated_user


@unauthenticated_user
def help_view(request):
    user_id = request.user.id

    context = {
        'username':request.user.username.capitalize(),
        'id': user_id
    }
    return render(request, 'first_app/help.html', context)

@unauthenticated_user
def budget_control(request):
    result = []
    today_month = datetime.today().month
    months = {0: 'JAN',
              1: 'FEV',
              2: 'MAR',
              3: 'ABR',
              4: 'MAI',
              5: 'JUN',
              6: 'JUL',
              7: 'AGO',
              8: 'SET',
              9: 'OUT',
              10: 'NOV',
              11: 'DEZ'
    }
    #gets the actual user
    actual_user = request.user
    #gets record from the database
    budget_registers = BudgetControl.objects.filter(user=actual_user)
    #calculates the sum of the goods
    goods_sum = budget_registers.filter(category='Good').aggregate(Sum('value'))['value__sum']
    #calculates the investments total value
    investments_sum = budget_registers.filter(category='Investment', month=months[today_month-1]).aggregate(Sum('value'))['value__sum']
    
    #calculates the total profit, total spends and sum for each month
    for month in range(12):
        result.append([0,0,0])
        profits = budget_registers.filter(category='Profit', month=months[month]).aggregate(Sum('value'))['value__sum']
        spends = budget_registers.filter(category='Spend', month=months[month]).aggregate(Sum('value'))['value__sum']        
        if profits:
            result[month][0] = int(profits)
        if spends:
            result[month][1] = int(spends)
        result[month][2] = result[month][0]-result[month][1]

    #calculates the annual total spends
    spends_sum = budget_registers.filter(category='Spend').aggregate(Sum('value'))['value__sum']

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
def add_record(request, user_id):
    user = User.objects.get(pk=user_id)

    AddRecordFormSet = inlineformset_factory(User,
                                             FixedValues,
                                             extra=1,
                                             can_delete=True,
                                             fields=('name',
                                                     'category',
                                                     'value',
                                                     'fixed'))

    if request.method == "POST":
        formset = AddRecordFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect('add', user_id=user.id)
        else:
            #parte para imprimir no terminal se houver algum erro na validação do formset
            print(formset.errors)

    formset = AddRecordFormSet(instance=user)

    context = {'formset': formset}

    return render(request, 'first_app/add_records.html', context)

#O update agora tem que ser feito em uma janela diferente
@unauthenticated_user
def update_record(request, pk):
    record = BudgetControl.objects.get(id=pk)
    form = BudgetControlForm(instance=record)
    if request.method == "POST":
        form = BudgetControlForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('budget')

    context = {'form':form,
               'operation_type':'Update'
    }
    return render(request, 'first_app/add_records.html', context)

@unauthenticated_user
def delete_record(request, pk):
    record = BudgetControl.objects.get(id=pk)
    if request.method == "POST":
        record.delete()
        return redirect("budget")

    context = {'item':record}
    return render(request, "first_app/delete.html", context)