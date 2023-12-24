from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalog_table, name="home"),
    path("add_column/", views.add_column, name="add_column"),
    path("change_table/", views.insert_into_table, name="insert_into_table"),
    path("pop", views.pop, name="pop"),
    path("pop_column", views.pop_column, name="pop_column"),
    path("change_table", views.change_table, name="change_table"),
    path("change", views.change, name="change"),
]
