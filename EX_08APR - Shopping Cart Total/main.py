#Declare empty lists for items and prices
items = []
prices = []
#Declare variable of type int for the number of items
n = int(input('Enter number of items: '))
#Loop through n
for i in range(n):
    #Prompt user to enter item
    item = input(f'Enter item {i + 1}: ')
    #Prompt user to enter price for item
    price = float(input('Enter price: '))
    #Add item to items list
    items.append(item)
    #Add price to prices list
    prices.append(price)
#Declare variable to pair the 2 lists and loop over them at the same time
item_price = zip(items, prices)
#Declare variable to store the sum of all prices
total = sum(prices)
#Declare variable for discount and set its value to 10
discount = 10
#Declare variable to store the final total after applying the discount
final_total = total - (discount * total / 100)
#Print section separator
print("---------------")
#Loop through each pair in zip, unpacking them into item and price
for item, price in item_price:
    #Print item and corresponding price
    print(item + ':', price)
#Print section separator
print("---------------")
#Print total
print(f'Total: {total}')
#Set condition for applying the discount (total > 100)
if total > 100:
    #Print the discount offered
    print(f' Discount: {discount}%')
    #Print the final total after discount
    print(f'Final total: ${final_total:.2f}')
#Set condition for total < 100
else:
    #Print the final total (no discount applied)
    print(f'Final total: ${total:.2f}')