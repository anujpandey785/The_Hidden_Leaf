from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','password2')