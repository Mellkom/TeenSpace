from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vakanсy
from django.contrib.auth.models import AbstractUser

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class PostForm(forms.ModelForm):
    class Meta:
        model = Vakanсy
        fields = ['name', 'category', 'author', 'cost', 'phone', 'course']

class ChildRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')

class ParentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')

class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')
