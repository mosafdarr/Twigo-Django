from django import forms
from .models import TweetModel

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = TweetModel
        fields = ['content', 'image']
