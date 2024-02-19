from django.contrib import admin
from main.models import Recipe, User, Tag, FoodType, Product, ProductMiddle, Unit


class ProductMiddleInline(admin.TabularInline):
    model = ProductMiddle


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductMiddleInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email"]


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name"]
