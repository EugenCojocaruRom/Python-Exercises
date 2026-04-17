#Have empty cart list
cart = []
#Prompt user for number of items
number_items = int(input('Enter the number of items in the cart: '))
#Loop through the number of items
for i in range(number_items):
    #Prompt user for item name
    name = input('Enter item name: ')
    #Prompt user for item price
    price = float(input('Enter price per unit: '))
    #Prompt user for quantity
    quantity = int(input('Enter quantity: '))
    #Add the item, price and quantity to the cart list
    cart.append((name, price, quantity))
#Create a totals list
totals = [price * quantity for (name, price, quantity) in cart]
#Loop through the items in the cart and totals lists -> use the zip function
for (name, price, quantity), total in zip(cart, totals):
    #Print the items and the corresponding totals
    print(f"{name}: ${total:.2f}")
#Calculate the grand total of the cart
grand_total = sum(totals)
#Print grand total
print(f"Cart total: ${grand_total:.2f}")
#Set conditions for displaying messages
if grand_total > 15:
    print('Cart total over $15. Stay on budget!')
else:
    print('Cart total below $15. Nice, you saved money!')