from django import forms
from django.forms import ModelForm
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class NewUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']