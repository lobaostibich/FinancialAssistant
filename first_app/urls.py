from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("time_management/", views.time_management, name="time"),
    path("budget_control/", views.budget_control, name="budget")
]