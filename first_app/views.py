from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum

from first_app.models import BudgetControl, FixedValues
from users.forms import BudgetControlForm, FixedValuesForm
from django.forms import inlineformset_factory
from users.decorators import unauthenticated_user


#variável criada para poder fazer a alteração na página de output caso novos dados tenham sido inseridos
organize_data = False

@unauthenticated_user
def help_view(request):

    context = {'username':request.user.username.capitalize()}

    return render(request, 'first_app/help.html', context)

#pega os dados que vieram da inserção facilitada(que possui os dados fixos e cria novos registros na tabela BudgetControl em cima desses dados)
@unauthenticated_user
def organize_data(request):

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

    #pegando usuário atual
    actual_user = request.user
    #buscando dados da tabela de dados fixos que são do usuário logado
    fixed_values_registers = FixedValues.objects.filter(user=actual_user)

    if fixed_values_registers.count() > 0:

        #jogar para a budgetContorl com a data desse mês
        for element in fixed_values_registers:
            register_instance = BudgetControl.objects.create(
                name=element.name,
                category=element.category,
                value=element.value,
                month=months[today_month-1],
                user=element.user
            )

        #depois apagar todos os dados que possuem valor variável da fixedValues
        variable_values = FixedValues.objects.filter(user=actual_user, fixed="VARIÁVEL")

        variable_values.delete()

    return render(request, 'first_app/organize.html')

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

    #essa parte trabalha em cima da tabela que fica na parte inferior da página, onde é possível adicionar, editar e remover dados dinamicamente
    user = User.objects.get(pk=request.user.id)

    BudgetControlFormSet = inlineformset_factory(User,
                                             BudgetControl,
                                             extra=1,
                                             can_delete=True,
                                             fields=('name',
                                                     'category',
                                                     'value',
                                                     'month'))

    if request.method == "POST":
        formset = BudgetControlFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()

            return redirect('budget')
        else:
            #parte para imprimir no terminal se houver algum erro na validação do formset
            print(formset.errors)

    formset = BudgetControlFormSet(instance=user)
    #vai até aqui a parte da tabela dinâmicamente alterada

    #pega o usuário atualmente logado
    actual_user = request.user
    #pega os registros do banco de dados
    budget_registers = BudgetControl.objects.filter(user=actual_user)

    #calcula a soma total das receitas
    profits_sum = budget_registers.filter(category='RECEITA').aggregate(Sum('value'))['value__sum']
    #calcula a soma dos investimentos no mês atual
    investments_sum = budget_registers.filter(category='INVESTIMENTO', month=months[today_month-1]).aggregate(Sum('value'))['value__sum']    
    #calcula a soma total dos gastos
    spends_sum = budget_registers.filter(category='GASTO').aggregate(Sum('value'))['value__sum']
    
    #calcula a soma total mensal da receita, gastos e o que sobra quando descontamos os gastos das receitas
    for month in range(12):
        result.append([0,0,0])
        profits = budget_registers.filter(category='RECEITA', month=months[month]).aggregate(Sum('value'))['value__sum']
        spends = budget_registers.filter(category='GASTO', month=months[month]).aggregate(Sum('value'))['value__sum']        
        if profits:
            result[month][0] = int(profits)
        if spends:
            result[month][1] = int(spends)
        result[month][2] = result[month][0]-result[month][1]

    #checa se a soma de investimentos é um valor vazio, se for coloca 0
    if investments_sum:
        investments_sum = int(investments_sum)
    else:
        investments_sum = 0

    #checa se a soma de gastos é um valor vazio, se for coloca 0
    if spends_sum:
        spends_sum = int(spends_sum)
    else:
        spends_sum = 0

    #checa se a soma de receitas é um valor vazio, se for coloca 0
    if profits_sum:
        profits_sum = int(profits_sum)
    else:
        profits_sum = 0

    return render(request, 'first_app/budget_control.html', {
        'formset': formset,
        'spends_sum': spends_sum,
        'profits_sum': profits_sum,
        'investments_sum':investments_sum,
        'result': result
    })

@unauthenticated_user
def add_record(request):

    user = User.objects.get(pk=request.user.id)

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

            return redirect('add')
        else:
            #parte para imprimir no terminal se houver algum erro na validação do formset
            print(formset.errors)

    formset = AddRecordFormSet(instance=user)

    context = {'formset': formset}

    return render(request, 'first_app/add_records.html', context)