#Print header
print("<-- RECIPE -->")
#Prompt user for the number of ingredients
num_ingredients = int(input("How many ingredients in the recipe? "))
#Prompt user to enter the number of servings
base_servings = int(input("How many servings based on the recipe? "))
#Prompt user to enter the number of desired servings
desired_servings = int(input("How many people are you cooking for? "))
#Create a scale factor for modifying the recipe according to the number of desired servings
scale_factor = desired_servings / base_servings
#Create empty list to hold the ingredients and the amounts
recipe = []
#Loop through the number of ingredients
for i in range(num_ingredients):
    #Prompt user to enter the ingredient
    ingredient = input(f"Ingredient {i + 1}: ").strip()
    #Prompt user to enter the amount
    ingredient_amount = float(input(f"Amount of {ingredient}: "))
    #Add ingredient and amount to the list
    recipe.append((ingredient.lower(), ingredient_amount))

#Print header and separator
print("\n<-- INGREDIENTS FOR BASE RECIPE -->")
print("-----------------------------------")
#Declare variable to calculate the maximum length of the ingredient name
max_length = max(len(ingredient) for ingredient, amount in recipe)
#Declare variable for displaying the ingredient amount and initialize it
display_amount = 0
#Loop through the recipe list
for ingredient, ingredient_amount in recipe:
    #Set conditions for displaying the ingredient amount
    if ingredient_amount.is_integer():
        #Display the ingredient amount as an integer
        display_amount = int(ingredient_amount)
    else:
        #Display the ingredient amount as a float
        display_amount = ingredient_amount
    #Set conditions for expressing quantities
    if ingredient in ["flour", "sugar", "milk", "water", "oil"]:
        if ingredient_amount == 1:
            #Print the ingredient and the amount
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount} cup")
        else:
            #Print the ingredient and the amount
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount} cups")
    elif ingredient in ["vanilla", "baking soda", "salt"]:
        if ingredient_amount.is_integer():
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount} tsp")
        else:
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount} tsps")
    else:
        if ingredient_amount.is_integer():
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount}")
        else:
            print(f" - {ingredient.capitalize():<{max_length}} -> {display_amount}")

#Print header and separator
print("\n<-- INGREDIENTS FOR UPDATED RECIPE -->")
print("--------------------------------------")
#Loop through the base recipe list
for i, (ingredient, ingredient_amount) in enumerate(recipe, start = 1):
    #Declare variable for displaying the updated ingredient amount
    updated_amount = ingredient_amount * scale_factor
    if ingredient in ["flour", "sugar", "milk", "water", "oil"]:
        if updated_amount == 1:
            #Print the ingredient and the amount
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {int(updated_amount)} cup")
        else:
            #Print the ingredient and the amount
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {updated_amount:.1f} cups")
    elif ingredient in ["vanilla", "baking soda", "salt"]:
        if updated_amount.is_integer():
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {int(updated_amount)} tsp")
        else:
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {updated_amount:.1f} tsps")
    elif ingredient in ["butter", "yeast"]:
        if updated_amount.is_integer():
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {int(updated_amount)} gram")
        else:
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {updated_amount:.1f} grams")
    else:
        if updated_amount.is_integer():
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {int(updated_amount)}")
        else:
            print(f"{i}. {ingredient.capitalize():<{max_length}} -> {updated_amount:.1f}")

#Print header and separator
print("\n<-- FINAL NECESSARY AMOUNTS -->")
print("-------------------------------")
#Filter the scaled amounts
scaled_amounts = [amount * scale_factor for ingredient, amount in recipe]
#filter the liquid ingredients
liquid_amounts = [amount * scale_factor for ingredient, amount in recipe if ingredient in ["milk", "water", "oil"]]
total_liquid = sum(liquid_amounts)
print(f"Total liquid needed: {total_liquid:.1f} cups")
#Filter the dry ingredients
dry_amounts = [amount * scale_factor for ingredient, amount in recipe if ingredient in ["flour", "sugar"]]
total_dry = sum(dry_amounts)
print(f"Total dry ingredients needed: {total_dry:.1f} cups")
#Filter the flavorings
flavor_amount = [amount * scale_factor for ingredient, amount in recipe if ingredient in ["vanilla", "baking soda", "salt"]]
total_flavor = sum(flavor_amount)
print(f"Total flavor needed: {total_flavor:.1f} tbsps")
#Filter the leavening ingredients
leavening_amount = [amount * scale_factor for ingredient, amount in recipe if ingredient in ["butter", "yeast"]]
total_leavening = sum(leavening_amount)
print(f"Total leavening ingredients needed: {total_leavening:.1f} grams")
#Filter the eggs
egg_amount = [amount * scale_factor for ingredient, amount in recipe if ingredient == "eggs"]
total_eggs = sum(egg_amount)
print(f"Total eggs needed: {total_eggs:.1f}")
