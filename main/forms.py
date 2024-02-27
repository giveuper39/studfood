from django import forms
from django.forms.widgets import TextInput, PasswordInput, EmailInput, NumberInput, CheckboxInput
from django.contrib.auth.forms import UserCreationForm
from main.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=EmailInput(attrs={"class": "form-control", "placeholder": "Электронная почта"}),
        max_length=100,
        min_length=10,
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}), max_length=65, min_length=5
    )


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=EmailInput(attrs={"class": "form-control", "placeholder": "Электронная почта"}))
    password1 = forms.CharField(widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Повторите пароль"})
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class GeneratorForm(forms.Form):
    days_num = forms.CharField(
        widget=NumberInput(
            attrs={
                "name": "days_num",
                "class": "form-control form-control-sm",
                "min": "1",
                "max": "15",
                "value": "7",
                "style": "width: 87.445px;font-size: 17px;background: transparent;border-style: solid;",
            }
        )
    )
    breakfast_check = forms.CharField(
        widget=CheckboxInput(
            attrs={
                "type": "checkbox",
                "name": "breakfast",
                "class": "form-check-input",
                "id": "formCheck-1",
                "checked": "",
            }
        )
    )
    lunch_check = forms.CharField(
        widget=CheckboxInput(
            attrs={"type": "checkbox", "name": "lunch", "class": "form-check-input", "id": "formCheck-2", "checked": ""}
        )
    )
    dinner_check = forms.CharField(
        widget=CheckboxInput(
            attrs={
                "type": "checkbox",
                "name": "dinner",
                "class": "form-check-input",
                "id": "formCheck-3",
                "checked": "",
            }
        )
    )
