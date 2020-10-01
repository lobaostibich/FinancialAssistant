from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class BudgetControl(models.Model):
    today_month = datetime.today().month
    months = [
        ('JANEIRO', 'JANEIRO'),
        ('FEVEREIRO', 'FEVEREIRO'),
        ('MARÇO', 'MARÇO'),
        ('ABRIL', 'ABRIL'),
        ('MAIO', 'MAIO'),
        ('JUNHO', 'JUNHO'),
        ('JULHO', 'JULHO'),
        ('AGOSTO', 'AGOSTO'),
        ('SETEMBRO', 'SETEMBRO'),
        ('OUTUBRO', 'OUTUBRO'),
        ('NOVEMBRO', 'NOVEMBRO'),
        ('DEZEMBRO', 'DEZEMBRO')
    ]
    categories = [
        ('RECEITA', 'RECEITA'),
        ('GASTO', 'GASTO'),
        ('INVESTIMENTO', 'INVESTIMENTO')
    ]

    user = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        null=True
    )
    category = models.CharField(
        max_length=12,
        choices=categories,
        null=True
    )
    value = models.FloatField(
        null=True
    )
    month = models.CharField(
        max_length=10,
        choices=months,
        null=True,
        default=months[today_month-1][0]
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return self.name

class FixedValues(models.Model):
    categories = [
        ('RECEITA', 'RECEITA'),
        ('GASTO', 'GASTO'),
        ('INVESTIMENTO', 'INVESTIMENTO')
    ]
    fixed_choices = [
        ('VARIÁVEL', 'VARIÁVEL'),
        ('FIXO', 'FIXO')
    ]

    user = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        null=True
    )
    category = models.CharField(
        max_length=12,
        choices=categories,
        null=True
    )
    value = models.FloatField(
        null=True
    )
    fixed = models.CharField(
        max_length=12,
        choices=fixed_choices,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return self.name
