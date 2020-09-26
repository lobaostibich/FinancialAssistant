from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class BudgetControl(models.Model):
    today_month = datetime.today().month
    months = [
        ('JAN', 'JANEIRO'),
        ('FEV', 'FEVEREIRO'),
        ('MAR', 'MARÇO'),
        ('ABR', 'ABRIL'),
        ('MAI', 'MAIO'),
        ('JUN', 'JUNHO'),
        ('JUL', 'JULHO'),
        ('AGO', 'AGOSTO'),
        ('SET', 'SETEMBRO'),
        ('OUT', 'OUTUBRO'),
        ('NOV', 'NOVEMBRO'),
        ('DEZ', 'DEZEMBRO')
    ]
    categories = [
        ('RECEITA', 'RECEITA'),
        ('GASTO', 'GASTO'),
        ('INVESTIMENTO', 'INVESTIMENTO'),
        ('BEM', 'BEM')
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
        max_length=3,
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
        ('INVESTIMENTO', 'INVESTIMENTO'),
        ('BEM', 'BEM')
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
