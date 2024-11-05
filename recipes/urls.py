from django.urls import path
from .views import RecipeListView, RecipeDetailView, get_queryset, add_recipe, update_recipe, delete_recipe, about_page

app_name = 'recipes'

## Maps the '' address to the home function-based view
urlpatterns = [
  path('about', about_page, name='about'),
  path('recipes/', RecipeListView.as_view(), name='list'),
  path('recipes/search', get_queryset, name='search'),
  path('recipes/add', add_recipe, name='add'),
  path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('recipes/update/<pk>', update_recipe, name='update'),
  path('recipes/delete/<pk>', delete_recipe, name='delete'),
]