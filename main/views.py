from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html")


def catalogue_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/recipes.html")


def generator_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/generator.html")


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        reg_form = RegisterForm()
        log_form = LoginForm()
        return render(request, "main/login.html", {"reg_form": reg_form, "log_form": log_form})
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)
        print(reg_form.is_valid())
        print(reg_form.errors)
        if reg_form.is_valid():
            user = reg_form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login_view(request=request, user=user)
            if user.is_authenticated:
                print("YAHOO")
            return redirect("home")
    reg_form = RegisterForm()
    log_form = LoginForm()
    return render(request, "main/login.html", {"reg_form": reg_form, "log_form": log_form})


def favourites_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/favourite.html")


def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/profile.html")

def recipe_view(request: HttpRequest) -> HttpResponse:
    return render()
