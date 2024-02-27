from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate, logout
from main.forms import LoginForm, RegisterForm, GeneratorForm
from main.models import User


def home_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())
    return render(request, "main/index.html")


def about_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())
    return render(request, "main/about.html")


def catalogue_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())
    return render(request, "main/recipes.html")


def generator_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())

    if request.method == "GET":
        gen_form = GeneratorForm()

    elif request.method == "POST":
        gen_form = GeneratorForm(request.POST)
        print(gen_form.is_valid())
        

    return render(request, "main/generator.html", {"gen_form": gen_form})


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
            login(request, user)
            if user.is_authenticated:
                print("YAHOO")
            return redirect("home")
        # TODO: доделать логин форму
    reg_form = RegisterForm()
    log_form = LoginForm()
    return render(request, "main/login.html", {"reg_form": reg_form, "log_form": log_form})


def favourites_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())
    user: User = request.user
    favs = user.favourites.all()
    return render(request, "main/favourite.html", {"favs": favs})


def profile_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        login(request, User.get_test_user())
    return render(request, "main/profile.html")


def recipe_view(request: HttpRequest) -> HttpResponse:
    return render()


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("home")
