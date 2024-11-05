from django import forms
from .models import Recipe

CHART_CHOICES = {
  ('#1', 'Bar Chart'),
  ('#2', 'Pie Chart'),
  ('#3', 'Line Chart')
}

class RecipeSearchForm(forms.Form):
  recipe_search = forms.CharField(max_length=120, label='Enter Recipe / Ingredient', required=False)
  chart_type = forms.ChoiceField(choices=CHART_CHOICES, label='Choose a Chart Type')

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['name', 'cooking_time', 'ingredients', 'pic']
    widgets = {
      'ingredients': forms.Textarea(attrs={'rows':4, 'cols':25}),
      }