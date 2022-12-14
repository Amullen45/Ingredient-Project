#import variables from ingredient scaper
import IngredientScraper

#create class to store recipes
class Recipe_list:
    #define a constructor to initialize storage
    def list(self):
        #define a list to hold the objects
        self.items=[]

    #define a method to add an object to the list
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
print(recipe)

#get ingredients list
ingredients = IngredientScraper.ingredient_list
print(ingredients)

#function to make recipe title a python variable
def python_variable(str):
    return str.lower().replace(' ', '_')

variable = python_variable(recipe)
print(variable)

recipes = Recipe_list()

recipes.add({'recipe': recipe, 'Ingredients': ingredients})

for i in range(len(recipes.items)):
    print(recipes.get(i))