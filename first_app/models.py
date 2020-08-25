from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

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
    categories = [
        ('Profit', 'PROFIT'),
        ('Spend', 'SPEND'),
        ('Investment', 'INVESTMENT'),
        ('Good', 'GOOD')
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(
        #verbose_name='Name:',
        max_length=255,
        null=True
    )
    category = models.CharField(
        max_length=10,
        choices=categories,
        null=True
    )
    value = models.FloatField(
        #verbose_name='Value of the expense:',
        default=0.0,
        null=True
    )
    month = models.CharField(
        #verbose_name='Month of the expense:',
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
