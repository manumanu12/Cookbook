from django.contrib.auth import get_user_model
# returns the user model that is currently active
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators
from crispy_forms.helper import FormHelper

class UserCreateForm(UserCreationForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


    # if botcatcher input is larger than 0 I will get an error as somebody entered sth in bot input in html tag

    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")

        widgets = {
            "username": forms.TextInput(attrs={"class":"sign"}),
        }

