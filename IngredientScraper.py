# Get the url from the textbox
from bs4 import BeautifulSoup, NavigableString
import requests

recipe_list = []

#create class to store recipes
class Recipe:

    #define a method to add an object to the list
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def add_recipe(name, ingredients):
        recipe_list.append({"Name": name, "Ingredients": ingredients})

    # #define a method to remove an object to the list
    # def remove(self, item):
    #     self.items.remove(item)

    # #define a constructor to initialize storage
    # def list(self):
    #     #define a list to hold the objects
    #     return self.recipes

    # # #define a method to retrieve an object from the list
    # def get(self, index):
    #  return self.items[index]
    
    # # #print Recipes
    # def print_recipes(self):
    #     for recipe in self.recipes:
    #          print(f"Recipe: {recipe['name']}")
    #          print("Ingredients:")
    #          for ingredient in recipe['ingredients']:
    #              print(f"  - {ingredient}")

# Variables

filename = 'Recipe.txt'

#url = 'https://www.gimmesomeoven.com/easy-beef-stroganoff-recipe/' #input('Enter a URL: ') # Working
#url = 'https://www.delish.com/cooking/recipe-ideas/a19636089/creamy-tuscan-chicken-recipe/' # Working
url = 'https://www.allrecipes.com/recipe/8489146/homemade-smash-burgers/' # New test site

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

#working to get all classes that contain list
class_ingredients = []
classes = []
for element in soup.find_all('div'):
    if element.get('class') is not None:
        classes.extend(element.get('class'))
for cls in classes:
    if 'ingredients' in cls:
        class_ingredients.append(cls)

#find header for name of recipe
for header in soup.find_all('h1'):
    title = header.text
    #print("title:", title)

#find if div contains <li> for the classes in class_ingredients
for li in class_ingredients:

    #find div element classes contained in class_ingredients
    div = soup.find('div', class_=li)
    
    # Find all the ingredients in the recipe
    ingredients = soup.find('div', attrs = {'class':li})


ingredient_list = []

for ingredient in ingredients:
    # Check that we're looking at a tag and not a NavigableString, if we are just continue
    if isinstance(ingredient, NavigableString):
        continue
    # Find all <li> tags from ingredient and print
    for li in ingredient.find_all('li'):
        ingredient_list.append(li.text)
#print("ingredients:", ingredient_list)

inglist = list(ingredient_list)
#push recipe to Recipe list on Recipelist
#print("Ingredients:", inglist)

#create variable out of the title
variable = title.replace(' ', '_').lower()

#creates new recipe with name: title, ingredients: inglist
recipe=Recipe.add_recipe(title, inglist)

#sets global recipe to equal variable (title.replace.lower)
globals()[variable] = recipe

#appends recipe into Recipe List
#recipe_list(recipe)
print(recipe_list)


# Same logic as above, but lets write to a file
# with open(filename, 'w') as file:
#     for ingredient in ingredients:
#         ingredient_list.append(ingredient.text)
#         #print(ingredient_list)
#         # Check that we're looking at a tag and not a NavigableString, if we are just continue
#         if isinstance(ingredient, NavigableString):
#             continue
#         # Find all <li> tags from ingredient and print
#         for li in ingredient.find_all('li'):
#             file.write(li.text)
#             file.write('\n')
        
# print(class_ingredients)
# print(list)
# print(ingredients)
