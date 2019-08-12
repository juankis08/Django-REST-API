from django.contrib import admin

# Register your models here.

from .models import User, Step, Ingredient, Recipe

admin.site.register(User)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)
