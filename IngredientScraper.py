
# Get the url from the textbox
from bs4 import BeautifulSoup
import requests


url = 'https://www.delish.com/cooking/recipe-ideas/a19636089/creamy-tuscan-chicken-recipe/' #input('Enter a URL: ')

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
div_list=[]
for list in class_ingredients:
    #print("list:", list)

    #find div element classes contained in class_ingredients
    div = soup.find('div', class_=list)
    #print('div:', div)

    #check if div contains list
    if div.find("ul") or div.find("ol"):
        div_list.append(div)

#print("div that contains list:", div_list)
    
# Find all the ingredients in the recipe
ingredients = soup.find_all('div', attrs = {'class':list})

#print ingredients
for ingredient in ingredients:

    print(ingredient.text)