from django.test import TestCase, Client
from .models import Recipe
from django.urls import reverse

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

# 2.5 tests

class RecipeViewsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up data for the view tests.
        cls.recipe = Recipe.objects.create(
            name='View Test Recipe',
            ingredients='Ingredient1,Ingredient2,Ingredient3',
            cooking_time=20,
            difficulty='Medium',
        )
    
    def test_home_page_status_code(self):
        # Test the home page is accessible and returns a HTTP 200 status.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_list_view(self):
        # Verify the recipe list view works and includes the recipe's name.
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Recipe')
    
    def test_recipe_detail_view(self):
        # Test the recipe detail view displays the correct recipe details.
        response = self.client.get(reverse('recipes:detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Recipe')
    
    def test_recipe_detail_view_with_nonexistent_recipe(self):
        # Check that a non-existent recipe detail view returns a 404 status.
        response = self.client.get(reverse('recipes:detail', args=[999]))
        self.assertEqual(response.status_code, 404)