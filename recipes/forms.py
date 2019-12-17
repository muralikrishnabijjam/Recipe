from django.forms import ModelForm
from .models import RecipeItems


class RecipeItemsForm(ModelForm):

    class Meta:
        model = RecipeItems
        fields = ["name", "ingredients", "process"]




