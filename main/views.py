from django.shortcuts import render

from django.http import HttpResponse, request


def index(req: request) -> HttpResponse:
    return HttpResponse("Hello, world!")
