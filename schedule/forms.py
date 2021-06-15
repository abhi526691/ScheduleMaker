from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.forms import ModelForm, fields, widgets
from .models import schedule
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class scheduleForm(forms.ModelForm):
    class Meta:
        model = schedule
        fields = '__all__'
        widgets = {
            'date' : forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'type' : 'date', 'placeholder' : 'date'}),
            'time' : forms.TextInput(attrs={'class': 'form-control', 'autofocus': True, 'type' : 'time', 'placeholder' : 'time'}),
            'work' : forms.Textarea(attrs={'class': 'form-control', 'autofocus': True, 'type' : 'text', 'placeholder' : 'Work'}),
        }








    
