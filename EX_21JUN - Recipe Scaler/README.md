EX\_21JUN - Recipe Scaler

The idea: You have a recipe with ingredients and amounts for a certain number of servings. The user enters how many servings they actually want to make, and the program scales every ingredient amount up or down, printing a nicely formatted list.

Requirements:

&#x20;- Start with a list of ingredients, each having a name and an amount (for a base number of servings, e.g. 4). You can hardcode this list or let the user build it.

&#x20;- Ask the user how many servings they want.

&#x20;- Calculate a scale factor (desired\_servings / base\_servings).

&#x20;- Use a for loop with enumerate() to print each ingredient's scaled amount, numbered.

&#x20;- Use a list comprehension somewhere — for example, to build a list of just the scaled amounts, or to filter ingredients above a certain quantity.

&#x20;- Print a nicely aligned summary using f-strings (padding the ingredient names so amounts line up in a column).



Bonus ideas (optional):

&#x20;- Round amounts sensibly (e.g. to 2 decimal places).

&#x20;- Handle a "halve the recipe" or "double the recipe" shortcut.

&#x20;- Validate that servings input is a positive number.

