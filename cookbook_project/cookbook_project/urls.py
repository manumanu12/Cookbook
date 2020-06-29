"""cookbook_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path("welcome/", views.WelcomePage.as_view(), name="welcome"),
    path("bye/", views.GoodbyePage.as_view(), name="bye"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("categories/", include("categories.urls", namespace="categories")),
    path("recipes/", include("recipes.urls", namespace="recipes")),
    path("about/", views.AboutView.as_view(),name="about"),
    path("signup/confirmation", views.SuccessSignUp.as_view(),name="signupconfirm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # The key to display an uploaded image is to add this function to the URL so it finds the image URL

