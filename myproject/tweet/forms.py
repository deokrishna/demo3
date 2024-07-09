from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','image']
