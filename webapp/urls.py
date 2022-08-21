from django.urls import path, URLPattern
from . import views

urlpatterns: list[URLPattern] = [
    path('', views.index, name="home"),
    path('add_expense', views.add_expense, name="add_expense"),
    path('update_expense', views.update_expense, name="update_expense"),
    path('delete_expense', views.delete_expense, name="delete_expense"),
    path('summary', views.summary, name="summary")
]