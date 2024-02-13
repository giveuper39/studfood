from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
    cooking_time = models.TimeField()
    cost = models.IntegerField()


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    password = models.CharField(max_length=65)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
