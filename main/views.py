from django.shortcuts import render

from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html")


def catalogue(request: HttpRequest) -> HttpResponse:
    return render(request, "main/catalogue.html")


def generator(request: HttpRequest) -> HttpResponse:
    return render(request, "main/generator.html")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "main/login.html")