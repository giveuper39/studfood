from django.contrib import admin
from main.models import Recipe, User, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email"]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]