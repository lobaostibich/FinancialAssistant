from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from first_app.models import BudgetControl


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BudgetControlForm(ModelForm):
    class Meta:
        model = BudgetControl
        fields = '__all__'