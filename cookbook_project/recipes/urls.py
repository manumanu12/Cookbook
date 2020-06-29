from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("new/",views.CreateRecipe.as_view(),name="create"),
    path("user/",views.UserRecipes.as_view(),name="userrecipe"),
    path("all/",views.AllRecipes.as_view(),name="all"),
    path("search/", views.SearchRecipes.as_view(),name="search"),
    path("delete/<int:pk>", views.DeleteRecipe.as_view(), name="delete"),
    path("update/<int:pk>", views.RecipeUpdate.as_view(), name="update"),
    path("<slug>/",views.RecipeDetail.as_view(), name="single"),
    path("send_data/<int:pk>/", views.send_recipe,name="senddata"),
    path("create/telegram_id/", views.CreateTelegramID.as_view(), name="create_id")
]