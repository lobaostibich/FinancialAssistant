from django.contrib import admin

from first_app.models import GroceryList, BudgetControl

admin.site.register(GroceryList)
admin.site.register(BudgetControl)