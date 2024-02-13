from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("catalogue/", views.recipes, name="recipes"),
    path("generator/", views.generator, name="generator"),
    path("login/", views.login, name="login"),
    path("favourite/", views.favourite, name="favourite"),
    path("profile/", views.profile, name="profile"),
]
