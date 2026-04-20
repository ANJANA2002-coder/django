from django import forms
from .models import Bookmark
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'url']


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']