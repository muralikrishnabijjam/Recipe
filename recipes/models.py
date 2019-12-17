from django.db import models


class RecipeItems(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=100)
    process = models.CharField(max_length=500)

    def __str__(self):
        return self.name



