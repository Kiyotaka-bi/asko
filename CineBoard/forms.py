from django import forms
from .models import Movie, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']