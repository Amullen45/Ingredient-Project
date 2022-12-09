# Get the url from the textbox
from bs4 import BeautifulSoup, NavigableString
import requests

# Variables

filename = 'Recipe.txt'

#url = 'https://www.gimmesomeoven.com/easy-beef-stroganoff-recipe/' #input('Enter a URL: ') # Working
url = 'https://www.delish.com/cooking/recipe-ideas/a19636089/creamy-tuscan-chicken-recipe/' # Working
#url = 'https://www.allrecipes.com/recipe/8489146/homemade-smash-burgers/' # New test site

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
#print(class_ingredients)

#find if div contains <li> for the classes in class_ingredients
for list in class_ingredients:

    #find div element classes contained in class_ingredients
    div = soup.find('div', class_=list)
    
# Find all the ingredients in the recipe
ingredients = soup.find('div', attrs = {'class':list})

#print ingredients
for ingredient in ingredients:
    # Check that we're looking at a tag and not a NavigableString, if we are just continue
    if isinstance(ingredient, NavigableString):
        continue
    # Find all <li> tags from ingredient and print
    for li in ingredient.find_all('li'):
        print(li.text)

# Same logic as above, but lets write to a file
with open(filename, 'w') as file:
    for ingredient in ingredients:
        # Check that we're looking at a tag and not a NavigableString, if we are just continue
        if isinstance(ingredient, NavigableString):
            continue
        # Find all <li> tags from ingredient and print
        for li in ingredient.find_all('li'):
            file.write(li.text)
            file.write('\n')
        
# print(class_ingredients)
# print(list)
# print(ingredients)