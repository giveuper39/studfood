from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate, logout
from main.forms import LoginForm, RegisterForm, GeneratorForm
from main.models import User, FoodType
import random


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
    menu = None
    if not request.user.is_authenticated:
        login(request, User.get_test_user())

    if request.method == "GET":
        gen_form = GeneratorForm()
        return render(request, "main/generator.html", {"gen_form": gen_form})
    elif request.method == "POST":
        gen_form = GeneratorForm(request.POST)
        if gen_form.is_valid():
            data = gen_form.cleaned_data
            user: User = request.user
            fav_list = list(user.favourites.all())
            print(FoodType.objects.all()[0].name)
            food_types = gen_form.food_types
            checks = tuple((True if data[f"{ft}_check"] == "True" else False) for ft in food_types)
            print(checks)
            days_num = int(data["days_num"])
            random.shuffle(fav_list)
            menu_list = tuple(
                (
                    (
                        list(
                            filter(lambda x: set(x.food_types.all()) & {FoodType.objects.all()[ind]} != set(), fav_list)
                        )[: 1 + days_num // 6]
                    )
                    if check
                    else []
                )
                for (ind, check) in enumerate(checks)
            )
            menu = [
                list(menu_list[j][(i // 6) % len(menu_list[j])] for i in range(days_num)) if checks[j] else None
                for j in range(3)
            ]
            if menu:
                return render(
                    request,
                    "main/generator.html",
                    {"gen_form": gen_form, "menu": menu, "days": range(0, days_num)},
                )
    gen_form = GeneratorForm()
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
