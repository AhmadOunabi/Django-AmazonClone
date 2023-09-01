from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )




class UserForm(forms.ModelForm):
    class Meta:
        user = User
        fields = ['username','email']


class UserActivationForm(forms.Form):
    code= forms.CharField(max_length=10)
    