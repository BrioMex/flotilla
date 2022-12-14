# First form not empty and can not be deleted
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')