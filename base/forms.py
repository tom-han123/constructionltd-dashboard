from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CreateregisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','phone_number', 'password1', 'password2']


