from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):

   class Meta:
        model = Recipe
        fields = ("name","ingredients","description","category","recipe_image")
        #creating widgets (add classes) to edit form input with css
        widgets = {
            "name" : forms.TextInput(attrs={"class":"control","placeholder":"Recipe´s title"}),
            "ingredients" : forms.Textarea(attrs={"class":"editable medium-editor-textarea postingredients"}),
            "description" : forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"}),
            "category" :forms.Select(attrs={"class":"control"})
        }

class RecipeUpdateForm(forms.ModelForm):

   class Meta:
        model = Recipe
        fields = ("name","ingredients","description","category","recipe_image")

        widgets = {
            "name" : forms.TextInput(attrs={"class":"control","placeholder":"Recipe´s title"}),
            "ingredients" : forms.Textarea(attrs={"class":"editable medium-editor-textarea postingredients"}),
            "description" : forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"}),
            "category" :forms.Select(attrs={"class":"control"})}