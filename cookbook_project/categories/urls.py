from . import views
from django.urls import  path
from categories.models import Category

app_name = "categories"

urlpatterns = [
    path("", views.ListCategory.as_view(), name="all"),
    path("new/", views.CreateCategory.as_view(), name="create"),
    path("recipes/in/<slug>", views.SingleCategory.as_view(), name="single"),
    path("delete/<int:pk>", views.DeleteCategory.as_view(), name="delete"),
]