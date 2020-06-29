from django.db import models
from django.urls import reverse
from categories.models import Category
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE) #related name is necessary to name the reverse relation from the User back to my model! https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django#:~:text=The%20related_name%20attribute%20specifies%20the,suffix%20_set%20%2C%20for%20instance%20User.&text=The%20Django%20documentation%20has%20more%20details.
    category = models.ForeignKey(Category, related_name="recipes", null=True, blank=False, on_delete=models.CASCADE) # Thanks to related name: I can e.g.: do: user.recipes.count -> as recipes is the related name I can use it to call all the recipes
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    name = models.CharField(max_length=200, unique=True, editable=True, validators=[alphanumeric,])
    description = models.TextField(editable=True)
    ingredients = models.TextField(editable=True, default="")
    slug = models.SlugField(allow_unicode=True,unique=True,default="")
    recipe_image = models.ImageField(upload_to="recipe_pics", blank=True, editable=True, default="")

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.name = self.name.lower()
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("categories:single", kwargs={"username":self.user.username, "pk":self.pk})

    class Meta: #how do we order the recipes?
        ordering = ["name"]
        unique_together = ["user", "description"] #we link each description with the user



