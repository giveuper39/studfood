from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("catalogue/", views.catalogue_view, name="catalogue"),
    path("generator/", views.generator_view, name="generator"),
    path("login/", views.login_view, name="login"),
    path("favourite/", views.favourites_view, name="favourite"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]
