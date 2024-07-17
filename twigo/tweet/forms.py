from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import TweetModel

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = TweetModel
        fields = ['content', 'image']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
