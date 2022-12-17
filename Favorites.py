favorites = []  # List to store the favorite recipes

while True:
    # Prompt the user for a recipe name
    print("Enter a recipe name, or 'q' to quit:")
    name = input()
    if name == 'q':
        break

    # Get the Recipe instance from the dictionary
    recipe = recipes.get(name)
    if recipe is None:
        print("Recipe not found")
    else:
        # Print the ingredients for the recipe
        print(recipe.ingredients)

        # Prompt the user to save the recipe as a favorite
        print("Save this recipe as a favorite? (y/n)")
        save = input()
        if save == 'y':
            favorites.append(recipe)

# Print the names of the favorite recipes
print("Your favorite recipes:")
for recipe in favorites:
    print(recipe.name)