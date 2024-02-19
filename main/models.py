from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField(max_length=4)


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=2000)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, default="Ужин")
    tags = models.ManyToManyField(Tag)
    products = models.ManyToManyField(Product, through="ProductMiddle")
    cooking_time = models.CharField(max_length=8)
    cost = models.IntegerField()


class ProductMiddle(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    password = models.CharField(max_length=65)
    favourites = models.ManyToManyField(Recipe)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
