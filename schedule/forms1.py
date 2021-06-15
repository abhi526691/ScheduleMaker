from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Re-Enter Your Password'})