from django.contrib import admin

from first_app.models import BudgetControl, FixedValues

admin.site.register(BudgetControl)
admin.site.register(FixedValues)