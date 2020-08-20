from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("prices/", views.prices, name="prices"),
    path("money_control/", views.money_control, name="money")
]