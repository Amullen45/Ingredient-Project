#import variables from ingredient scaper
import IngredientScraper

#create class to store recipes
class Recipe_list:
    #define a constructor to initialize storage
    def list(self):
        #define a list to hold the objects
        self.items=[]

    #define a method to add an object to the list
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    #define a method to remove an object to the list
    def remove(self, item):
        self.items.remove(item)

    #define a method to retrieve an object from the list
    def get(self, index):
        return self.items[index]
    
#get recipe name
recipe = IngredientScraper.title
#print(recipe)

#get ingredients list
ingredients = IngredientScraper.ingredient_list
#print(ingredients)

# Strip whitespace from each element in the array
cleaned_array = [x.strip() for x in ingredients]

# Remove empty elements from the array
cleaned_array = list(filter(None, cleaned_array))

#print(cleaned_array)

# Separate the string into a list where each item is separated by "\n"
string_list = cleaned_array[0].replace('\xa0', ' ').split("\n")
#print(string_list)

#function to make recipe title a python variable
def python_variable(str):
    return str.lower().replace(' ', '_')

variable = python_variable(recipe)
#print(variable)

recipes = Recipe_list()

recipes.add({'recipe': recipe, 'Ingredients': string_list})

for i in range(len(recipes.items)):
    print(recipes.get(i))
