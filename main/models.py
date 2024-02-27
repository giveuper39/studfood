from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=15, unique=True)

    @classmethod
    def get_default(cls):
        unit, created = cls.objects.get_or_create(name="шт.")
        return unit.pk

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)

    @classmethod
    def get_default(cls):
        food_type, created = cls.objects.get_or_create(name="Ужин")
        return food_type.pk

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=2000)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, default=FoodType.get_default)
    tags = models.ManyToManyField(Tag)
    products = models.ManyToManyField(Product, through="ProductMiddle")
    cooking_time = models.CharField(max_length=8)
    cost = models.IntegerField()
    photo = models.ImageField(upload_to="main_pics", default="86.jpg")

    def __str__(self):
        return self.name


class ProductMiddle(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.FloatField(max_length=5)
    units = models.ForeignKey(Unit, on_delete=models.CASCADE, default=Unit.get_default)

    class Meta:
        unique_together = ("product", "recipe")


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    password = models.CharField(max_length=65)
    favourites = models.ManyToManyField(Recipe)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    @classmethod
    def get_test_user(cls):
        test_recipes = (Recipe.objects.get(name="TestFood1"), Recipe.objects.get(name="TestFood2"))
        user, _ = cls.objects.get_or_create(email="qwertytest@gmail.com", password="12345678", )
        user.favourites.set(test_recipes)
        return user
