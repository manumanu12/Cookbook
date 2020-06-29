from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from braces.views import SelectRelatedMixin
from . import forms
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import (render, get_object_or_404)
import telegram
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import strip_tags
from telegram_profile.models import TelegramProfile
from django.db import IntegrityError
from django.http import HttpResponse

class AllRecipes(generic.ListView, LoginRequiredMixin):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    paginate_by = 8


class RecipeDetail(SelectRelatedMixin, LoginRequiredMixin, generic.DetailView):
    model = Recipe
    select_related = ("category", "user")  # select category from the related models
    # if only 1 select related: always add the , otherwise it would return an error as string and not a list or tuple!


class CreateRecipe(SelectRelatedMixin, LoginRequiredMixin, generic.CreateView):
    model = Recipe
    form_class = forms.RecipeForm

    def form_valid(self, form):  # default function, we always / often use when we have create view and mixins
        try:
            self.object = form.save(commit=False) # need this function + commit = False to avoid: Not Null constraint error
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form) #form_valid requests a response object -> we need to return a response instead of get (e.g. get-> reverse)
        except IntegrityError: # Integrity error means - not unique
            return HttpResponse("Failed to save the recipe! Make sure your recipe name is unique! " # Response in case that form is unable to save recipe
                                "It is forbidden to use a recipe name twice! ")

    def get_success_url(self):
        return reverse_lazy("categories:all")


class DeleteRecipe(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Recipe
    select_related = ("category",)

    def get_success_url(self):
        return reverse("categories:single", kwargs={"slug": self.object.category.slug})


class RecipeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Recipe
    # fields = ["name","ingredients","description","category"] -> specified in forms.py already, error if I would redefine here
    form_class = forms.RecipeUpdateForm
    template_name = "recipes/update_recipe.html"

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse(
                "Failed to update the recipe! Make sure your recipe name is unique! "  # Response in case that form is unable to update recipe
                "It is forbidden to use a recipe name twice! ")


    def get_success_url(self):
        return reverse("categories:all")


class UserRecipes(LoginRequiredMixin, generic.ListView, MultipleObjectMixin):
    model = Recipe
    template_name = "recipes/user_recipes.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        object_list = Recipe.objects.filter(
            user=self.request.user)  # I loop through the object_list in my template, hence object list are all recipes from this category
        context = super(UserRecipes, self).get_context_data(object_list=object_list, **kwargs)
        return context


class SearchRecipes(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = "recipes/search.html"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get(
            "searchrecipe")  # searchrecipe is the name of our input form, means: the value we inter in this form will be saved here
        object_list = Recipe.objects.filter(name__icontains=query)
        return object_list


class CreateTelegramID(LoginRequiredMixin,generic.TemplateView):
    model = Recipe
    template_name = "recipes/create_telegram.html"


# create telegram bot:

URL = settings.BOT_URL
my_token = settings.BOT_TOKEN


class LazyEncoder(DjangoJSONEncoder): # this class is only necessary in case I use serialize to work with json data to return it in a dict

    def default(self, object):
        if isinstance(object, dict):
            return str(object)
        return super().default(object)

# serialize("json",User.objects.filter(username=request.user),fields=("username") cls=LazyEncoder

def bot(request, msg, chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=msg)



def send_recipe(request, pk):
    try:
        if request.method == "POST":
            data_option = str(request.POST[
                                  "testselect"])  # testselect is the select form in recipe_detail.html with which I select 1 of the 2 options
            if data_option == "Ingredients":
                recipe = get_object_or_404(Recipe, pk=pk)
                recipe_name = recipe.name.upper()
                ingredients = recipe.ingredients
                ingredients = ingredients.split("<p>")
                ingredients = "\n".join(ingredients)
                ingredients = strip_tags(ingredients)
                message = f"{recipe_name}: \n {ingredients}"

                user = TelegramProfile.objects.get(
                    user=request.user)  # use get instead of filter! filter returns the name but can t use it as object, with get I get the object and I can use the attributes on it!
                chat_id = user.telegram_chat_id
                bot(request, message, chat_id)
                return render(request, "recipes/recipe_send_conf.html")
            elif data_option == "Ingredients & Description":
                recipe = get_object_or_404(Recipe, pk=pk)
                recipe_name = recipe.name.upper()  # recipe name
                ingredients = recipe.ingredients
                ingredients = ingredients.split("<p>")
                ingredients = "\n".join(ingredients)
                ingredients = strip_tags(
                    ingredients)  # we grab recipes ingredients and mute them, split at p tag, then add a new line and join them then remove tags
                recipe_description = recipe.description
                recipe_description = recipe_description.split("<p>")
                recipe_description = "\n".join(recipe_description)
                recipe_description = strip_tags(recipe_description)
                message = f"{recipe_name}: \n {ingredients} \n \n {recipe_description}"

                user = TelegramProfile.objects.get(user=request.user)
                chat_id = user.telegram_chat_id
                bot(request, message, chat_id)
                return render(request, "recipes/recipe_send_conf.html")
        else:
            return render(request, "recipes/create_telegram.html")
    except Exception:
        return render(request, "recipes/create_telegram.html")


