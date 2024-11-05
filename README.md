# Recipe App
## Overview
The recipe app is a web application built with Python using the Django framework with recipes being stored in a SQLite database. 
Recipe app allows users to sign up, login, and logout; while using the application, users can create, modify, and search recipes. 
While looking at a list of recipes, users can also request more details about a recipe -- such as name, cooking time, ingredient list, and difficulty (which is automatically calculated by cooking time and number of ingredients)

## Static and Media files
- Utilizes `whitenoise` to store static files such as css, js, and static image files.
- Uses `django-storages` and the Heroku add-on `bucketeer` to manage user-uploaded files (e.g. images uploaded for a recipe)

## Apps
### recipes

<details>
<summary> models </summary>
  
#### The Recipe model includes the following:
  
  - `name` ( CharField, max length of 120 )
  - `cooking_time` ( Positive Integer, must be in the range of 1 - 100, should be given in minutes )
  - `ingredients` ( CharField, max length of 200, each ingredient should be separated by a comma )
  - `pic` (ImageField that uploads to the `media/recipes` folder
  - Defines the `calc_difficulty` function to calculate a recipes difficulty given the num of ingredients and cooking time
  - Defines the `get_ingredient_list` function that strips whitespaces from ingredients list and then splits the string at commas
  - Defines the  `get_absolute_url` function that creates url for object using its primary key

</details>

<details>
<summary> tests </summary>

#### `RecipeModelTest` creates the following test data:
  ```
  name = 'Tea'
  cooking_time = 5
  ingredients = 'tea leaves, water, sugar'
  ```

#### `RecipeModelTest` includes the following tests:

##### `test_recipe_name`
  > checks if object name and the verbose_name of the `name` field are equal

##### `test_recipe_name_max_length`
  > checks if the parameter `max_length` for `name` equals 120

##### `test_cooking_time_min`
  > checks if the `cooking_time` value is between 1 and 100

##### `test_cooking_time_type`
  > checks if the `cooking_time` value is an integer

##### `test_ingredients_max_length`
  > checks if the parameter `max_length` for `ingredients` equals 200

##### `test_recipe_difficulty`
  > calls `calc_difficulty()` on test recipe to ensure it calculates the expected 'Easy' difficulty

##### `test_get_absolute_url`
  > calls `get_absolute_url()` on test recipe to ensure the url it produces equals `/recipes/1`

##### `test_ingredient_list`
  > calls `get_ingredient_list()` on test recipe to get length of ingredient list and compares to expected value

#### `RecipeFormTest` creates the following test data:
  ```
  name = 'Tea'
  cooking_time = 5
  ingredients = 'tea leaves, water, sugar'

  name = 'Lemon Rice'
  cooking_time = 30
  ingredients = 'lemons, rice, water'
  ```

#### `RecipeFormTest` includes the following tests:

##### `test_search_request`
  > posts search data to `/recipes/search`, expects a status code of 200

##### `test_form_valid`
  > passes search data to `RecipeSearchForm()` and checks `is_valid()`

##### `test_search_ingredient`
  > posts ingredient search data to `/recipes/search` and decodes response to check if both recipes are present

##### `test_search_recipe`
  > posts recipe name search data to `/recipes/search` and decodes response to check if recipe is present

</details>

<details>
<summary> views </summary>
  
##### home
  > Redirects user to `login` so they can be authenticated

#### login_view
  > Accepts web request

  > Authenticates form data; if user is authenticated, they are redirected to `recipes:list`

  > If they are not authenticated, an error message is returned

#### logout_view
  > Accepts web request

  > Returns `success.html` template to show user they have been successfully signed out

  > Template also provides button back to `login` if the user wishes to log back in

#### about_page
  > Accepts web request

  > Returns `recipes/about.html`

#### delete_recipe
  > Accepts web request and primary key

  > Gets recipe object based on primary key then deletes object

  > Redirects user to List view after deletion

#### update_recipe
  > Accepts web request and primary key

  > Gets recipe object based on primary key then if method is POST, form data is gathered

  > If form is valid, form is saved and the recipe is updated

#### add_recipe
  > Accepts web request and primary key

  > Gets recipe object based on primary key then if method is POST, form data is gathered

  > If form is valid, form is saved and the recipe is created

#### get_queryset
  > Accepts web request

  > Gets search term and selected chart type from submitted form

  > Filters recipes based on search term then created pandas DataFrame from values

  > Calls `get_chart()` from `utils.py` to generate chart based on DataFrame

##### RecipeListView
  > Class-based view that produces list view of the recipes

  > Returns the `recipes/recipe_list.html` template

##### RecipeDetailView
  > Class-based view that produces a detailed view of the specified recipe
  
  > Returns the `recipes/recipe_detail.html` template

</details>
