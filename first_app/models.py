from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class GroceryList(models.Model):
    name = models.CharField(
        verbose_name='Name of the product:',
        max_length=255
    )
    quantity = models.FloatField(
        verbose_name='Quantity:',
        default=1.0
    )
    unit_price = models.FloatField(
        verbose_name='Unit Price:',
        default=0.0
    )
    created_at = models.DateField(
        auto_now_add=True
    )

class BudgetControl(models.Model):
    today_month = datetime.today().month
    months = [
        ('JAN', 'JANUARY'),
        ('FEB', 'FEBRUARY'),
        ('MAR', 'MARCH'),
        ('APR', 'APRIL'),
        ('MAY', 'MAY'),
        ('JUN', 'JUNE'),
        ('JUL', 'JULY'),
        ('AUG', 'AUGUST'),
        ('SEP', 'SEPTEMBER'),
        ('OCT', 'OCTOBER'),
        ('NOV', 'NOVEMBER'),
        ('DEC', 'DECEMBER')
    ]
    #fixed expenses
    fixed_expense_name = models.CharField(
        verbose_name='Name of the fixed expense:',
        max_length=255
    )
    fixed_expense_price = models.FloatField(
        verbose_name='Value of the expense:',
        default=0.0
    )
    fixed_expense_month = models.CharField(
        verbose_name='Month of the expense:',
        max_length=3,
        choices=months,
        default=months[today_month-1][0]
    )
    #fixed earnings
    fixed_earnings_name = models.CharField(
        verbose_name='Name of the fixed earn:',
        max_length=255
    )
    fixed_earnings_price = models.FloatField(
        verbose_name='Value of the earn:',
        default=0.0
    )
    fixed_earnings_month = models.CharField(
        verbose_name='Month of the earn:',
        max_length=3,
        choices=months,
        default=months[today_month-1][0]
    )
    #variable costs
    variable_costs_name = models.CharField(
        verbose_name='Name of the variable cost:',
        max_length=255
    )
    variable_costs_price = models.FloatField(
        verbose_name='Value of the variable cost:',
        default=0.0
    )
    variable_costs_month = models.CharField(
        verbose_name='Month of the variable cost:',
        max_length=3,
        choices=months,
        default=months[today_month-1][0]
    )
    #investiments
    investment_name = models.CharField(
        verbose_name='Name of the investment:',
        max_length=255
    )
    investment_price = models.FloatField(
        verbose_name='Value of the investment:',
        default=0.0
    )
    investment_month = models.CharField(
        verbose_name='Month of the investment:',
        max_length=3,
        choices=months,
        default=months[today_month-1][0]
    )