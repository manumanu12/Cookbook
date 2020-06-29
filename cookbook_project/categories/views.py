from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Category
from django.utils.text import slugify
from recipes.models import Recipe
from recipes.forms import RecipeForm
from django.views.generic.list import MultipleObjectMixin
from django.db import IntegrityError
from django.http import HttpResponse
# Create your views here


class CreateCategory(LoginRequiredMixin,generic.CreateView):
    fields = ("name","description")
    model = Category

    def get_success_url(self):
        return reverse_lazy("categories:all")

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False) # need this function + commit = False to avoid: Not Null constraint error
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form) #form_valid requests a response object -> we need to return a response instead of get (e.g. get-> reverse)
        except IntegrityError: # Integrity error means - not unique
            return HttpResponse("Failed to save the Category! Make sure your category name is unique! " # Response in case that form is unable to save recipe
                                "It is forbidden to use a category name twice! ")


class SingleCategory(LoginRequiredMixin,generic.DetailView,MultipleObjectMixin): # I need MultipleObjectMixin so that pagination works
    model = Category
    paginate_by = 8

    def get_context_data(self, **kwargs):
        object_list = Recipe.objects.filter(category=self.get_object()) # I loop through the object_list in my template, hence object list are all recipes from this category
        context = super(SingleCategory,self).get_context_data(object_list=object_list,**kwargs)
        context["form"] = RecipeForm
        return context


class ListCategory(LoginRequiredMixin, generic.ListView):
    model = Category
    paginate_by = 8

class DeleteCategory(LoginRequiredMixin, generic.DeleteView):
    model = Category

    def get_success_url(self):
        return reverse("categories:all")

