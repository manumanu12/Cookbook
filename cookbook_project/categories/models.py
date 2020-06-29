from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.') # validator, only allow alphanumeric input for name

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, validators=[alphanumeric,])
    description = models.TextField(blank=True, default="", max_length=48)
    slug = models.SlugField(allow_unicode=True,unique=True,default="")


    def __str__(self):
        return self.name

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.name = self.name.lower()
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("categories:single",kwargs={"slug":self.slug})

    class Meta:
        ordering = ["name"]
