#Create empty list
grocery_list = []
#Prompt user for number of items
number_items = int(input('Enter the number of items on the list: '))
#Loop through the number of items and add a name and price for each of them
for i in range(number_items):
    #Enter name of item
    name = input("Item name: ")
    #Enter price of item
    price = float(input("Price ($): "))
    #Add the new item to the list
    grocery_list.append((name, price))
#Print the list
print("\nYour grocery list:", grocery_list)
#Extract only the prices from the list
prices = [price for name, price in grocery_list]
print("Prices:", prices)
#Declare a variable and initialize it to 0
total = 0
#Loop through each individual value from the prices list
for price in prices:
    #Calculate the total price of the items on the list
    total += price
#Print the total
print(f"Total: ${round(total, 2)}")
#Set condition for applying 10% discount if total > 40
if total > 40:
    #Calculate the total after applying the discount
    total = total - (total * 0.10)
    #Print the new total (with discount)
    print(f"Discount applied! New total: ${round(total, 2)}")
#Loop through the grocery list
for name, price in grocery_list:
    #Set condition for price > 8
    if price > 8:
        #Print each item whose prices > 8
        print(f"Expensive item: {name} - ${price}")
