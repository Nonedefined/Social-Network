from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.SlugField(label='Username',  widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Password confirmation',  widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.SlugField(label='Username',  widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "mobile", "address", "bio", "photo"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.TextInput(attrs={"class": "form-control"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text", "photo"]
        labels = {
            "text": ""
        }
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "What do you think?"}),
        }


class MessageChatForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text"]
        labels = {
            "text": ""
        }
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Type a message"}),
        }


class CommentForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control",
                                                            "rows": 4,
                                                            "placeholder": "What is your view?"}))
