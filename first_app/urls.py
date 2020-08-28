from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.budget_control, name="budget"),
    path("add_record/", views.add_record, name="add"),
    path("update_record/<str:pk>/", views.update_record, name="update"),
    path("delete_record/<str:pk>/", views.delete_record, name="delete"),
    path("help/", views.help_view, name="help")
]