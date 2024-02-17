from django import forms
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=EmailInput(attrs={"class": "form-control", "placeholder": "Электронная почта"}),
                            max_length=100, min_length=10)
    password = forms.CharField(widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}),
                               max_length=65, min_length=5)


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=EmailInput(attrs={"class": "form-control", "placeholder": "Электронная почта"}))
    password1 = forms.CharField(widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Повторите пароль"}))

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
