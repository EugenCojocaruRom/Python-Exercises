#Print header and separator
print("<== Sale Price Tag Printer ==>\n"
      "------------------------------")

#Create function for validating user input (float values)
def get_float(prompt, minimum=0, maximum=None):
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print(f"The value must be at least {minimum}. Please try again.")
                continue
            if maximum is not None and value > maximum:
                print(f"The value must be at most {maximum}. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a correct value.")

#Create function for validating user input (int values)
def get_int(prompt, minimum=1):
    while True:
        try:
            user_value = int(input(prompt))
            if user_value < minimum:
                print(f"The value must be at least {minimum}. Please try again.")
                continue
            return user_value
        except ValueError:
            print("Please enter a correct value.")

#Create empty list to store the prices
prices = []
#Prompt user to enter a number of price tags
num_price_tags = get_int("Enter the number of price tags: ")
#Loop over the number of price tags
for i in range(num_price_tags):
    #Prompt user to enter the price
    price_tag = get_float(f"Enter the price on tag {i+1}: ")
    #Add the price tag to the prices list
    prices.append(price_tag)

print()
#Prompt user to enter the discount percentage
discount = get_float("Enter the discount percentage (%): ", maximum=100)
#Prompt user to enter the item value for which the discount is applied
item_value = get_float("Enter the item value for applying the discount: ")

print("\n== Price Tags ==")
#Create a list for sale prices - apply the discount for items > item value
sale_prices = [x * (1 - discount / 100) if x > item_value else x for x in prices]
#Declare variable for counting the discounted sales and initialize it
discounted_count = 0
#Loop over the sales prices and prices lists and print the final sale prices
for i, (original, sale) in enumerate(zip(prices, sale_prices), 1):
    if original > item_value:
        #Increment the discounted sales counter
        discounted_count += 1
        print(f"Item {i}: {original:.2f} -> {sale:.2f} (SALE!)")
    else:
        print(f"Item {i}: {original:.2f} -> {sale:.2f}")

print()
print(f"Items discounted: {discounted_count}")
#Calculate and print the total saved amount
total_saved = sum(prices) - sum(sale_prices)
print(f"Total saved: {total_saved:.2f}")
