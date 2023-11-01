from django.db import models


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
