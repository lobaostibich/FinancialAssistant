from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.budget_control, name="budget"),
    path("add_record/", views.add_record, name="add"),
    path("organize/", views.organize_data, name="organize"),
    path("help/", views.help_view, name="help")
]