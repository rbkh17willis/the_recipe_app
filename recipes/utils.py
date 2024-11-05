from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from recipes.models import Recipe

def get_recipename_from_id(val):
  recipename = Recipe.objects.get(id=val)
  return recipename

def get_graph():
  # creates a BytesIO buffer for the image
  buffer = BytesIO()

  plt.savefig(buffer, format='png')

  # set cursor to the beginning of the stream
  buffer.seek(0)

  # retrieves content of the file
  image_png = buffer.getvalue()

  # encodes the bytes-like objetcs
  graph = base64.b64encode(image_png)

  # decodes to get the string as output
  graph = graph.decode('utf-8')

  #frees up memoery of buffer
  buffer.close()

  return graph

def get_chart(chart_type, data, search):
  #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
  #AGG is preferred solution to write PNG files
  plt.switch_backend('AGG')

  #specify figure size
  fig =plt.figure(figsize=(7,5))
  fig.set_facecolor('#d6dbdf4d')
  
  recipes_found = len(data)
  total_recipes = Recipe.objects.count()

  ing_list = []
  ing_num = []

  limited_num = []
  limited_ing = []
  
  for list in data['ingredients']:
    data_list = list.split(', ')
    for ing in data_list:
      if ing.title() not in ing_list:
        ing_list.append(ing.title())

  for ing in ing_list:
    num_recipe = len(Recipe.objects.filter(ingredients__icontains=ing))
    ing_num.append(num_recipe)
    if ((num_recipe / len(ing_num)) * 100) >= 25:
      limited_num.append(num_recipe)
      limited_ing.append(ing.title())

  #select chart_type based on user input from the form
  if chart_type == '#1':
      #plot horizontal bar chart based on ingredient on y-axis and 
      # how many recipes they are found in on x-axis
      if search == '':
        plt.barh(limited_ing, limited_num, color=['#7e9798'])
      else:
        plt.barh(ing_list, ing_num, color=['#7e9798'])
      plt.xlabel('Found in # of Recipes')
      plt.xlim(right=total_recipes)

  elif chart_type == '#2':
      #generate pie chart based percentage of recipes found
      if search == '':      
        labels = limited_ing
        sizes = limited_num

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#7e9798', '#d6dbdf', '#B6BBB6', '#BBC0C3', '#DFDAD6'])
      else:
        labels= f'Recipes with {search.title()}', 'Total Recipes'
        sizes = [recipes_found, total_recipes]
        
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#7e9798', '#d6dbdf'])

  elif chart_type == '#3':
      #plot line chart based on ingredient on x-axis and 
      # how many recipes they are found in on y-axis
      if search == '':      
        plt.plot(limited_ing, limited_num, color='#7e9798', linewidth=2)
      else:
        plt.plot(ing_list, ing_num, color='#7e9798', linewidth=2)
      plt.grid(True, linewidth=0.5)
      plt.xticks(rotation=25)
      plt.yticks(range(total_recipes+1))
      plt.ylim(top=total_recipes)
      plt.title('# of Recipes Found with Ingredients')

  else:
      print ('unknown chart type')

  #specify layout details
  plt.tight_layout()

  #render the graph to file
  chart =get_graph() 
  return chart  