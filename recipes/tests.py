from django.test import TestCase, Client
from .models import Recipe
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeSearchForm

# 2.4 tests
class RecipeModelTest(TestCase):
    # set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name = "Tea",
            ingredients = "Tea leaves, Sugar, Water",
            cooking_time = 5,
            difficulty = "Easy"
        )

    # NAME
    def test_recipe_name(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'name' field and use it to query its data
        max_length = recipe._meta.get_field("name").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 50)

    # INGREDIENTS
    def test_ingredients_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field("ingredients").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 225)

    # COOKING TIME
    def test_cooking_time_value(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # get metadata for 'cooking_time' field and use it to query its data
        cooking_time_value = recipe.cooking_time


    # DIFFICULTY
    def test_difficulty_calculation(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # compare the value to the expected result
        self.assertEqual(recipe.difficulty, "Easy")


class RecipeFormTest(TestCase):

  def setUpTestData():
    Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea leaves, water, sugar')
    Recipe.objects.create(name='Lemon Rice', cooking_time=30, ingredients='lemons, rice, water')

    User.objects.create_user(username='testuser', password='testpassword')

  ## TEST SEARCH FUNCTION
  def test_search_request(self):
    client = Client()
    client.login(username='testuser', password='testpassword')

    data = {'recipe_search': 'sugar', 'chart_type': '#1'}
    response = client.post('/recipes/search', data)

    self.assertEqual(response.status_code, 200)

  def test_form_valid(self):
    data = {'recipe_search': 'sugar', 'chart_type': '#1'}
    response = RecipeSearchForm(data)

    self.assertTrue(response.is_valid())
  
  def test_search_ingredient(self):
    client = Client()
    client.login(username='testuser', password='testpassword')

    input = {'recipe_search': 'water', 'chart_type': '#1'}
    response = client.post('/recipes/search', input)
    data = response.content
    
    self.assertTrue('Tea' in data.decode())
    self.assertTrue('Lemon Rice' in data.decode())

  def test_search_recipe(self):
    client = Client()
    client.login(username='testuser', password='testpassword')

    input = {'recipe_search': 'lemon rice', 'chart_type': '#1'}
    response = client.post('/recipes/search', input)
    data = response.content
    
    self.assertTrue('Lemon Rice' in data.decode())