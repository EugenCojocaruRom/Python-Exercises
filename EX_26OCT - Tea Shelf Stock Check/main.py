#Print header and separator
print("<== Tea Shelf Stock Check ==>")
print("-----------------------------")

#Have a list of tea types and quantities
stock = [
    ("Green", 250),
    ("Earl Grey", 40),
    ("Chamomile", 0),
    ("Peppermint", 120),
    ("Jasmine", 15),
    ("Black", 300),
    ("Oolong", 50),
    ("Rooibos", 300)
]

print("== Current Stock ==")
#Loop over the stock list and print each tea type and its quantity
for i, (tea, qty) in enumerate(stock, start=1):
    print(f"{i}. {tea} - {qty}g")

#Calculate and print the total quantity
total_qty = 0 #total_qty = sum(qty for _, qty in stock)
for _, qty in stock:
    total_qty += qty
print(f" -> Total tea quantity: {total_qty}g")

print()
#Find the tea types low on stock (less than 50 but different from 0)
low_stock = [tea for tea, qty in stock if 50 > qty > 0]
#Find the tea types that are out of stock (0 grams)
zero_stock = [tea for tea, qty in stock if qty == 0]
#Print the teas with low stock and zero stock
if not low_stock and not zero_stock:
    print("Stock OK for all teas.")
else:
    if low_stock:
        print(f"Low stock for {', '.join(low_stock)}. You should order some more.")
    if zero_stock:
        print(f"Out of stock: {', '.join(zero_stock)}. You should order some more.")

#Print header
print("\n== Stock Status ==")
for tea, qty in stock:
    if qty >= 50:
        print(f"{tea}: OK")
    elif 1 <= qty < 50:
        print(f"{tea}: LOW")
    else:
        print(f"{tea}: EMPTY")

#Find and print the name of the tea with the most grams in stock
best_teas = []
best_qty = -1
for tea, qty in stock:
    #If this tea has more qty than best_qty, the best teas list receives the tea as value; best qty is updated
    if qty > best_qty:
        best_teas = [tea]
        best_qty = qty
    elif qty == best_qty:
        #The tea is added to the best teas list
        best_teas.append(tea)
if not best_teas:
    print(" -> No teas in stock list.")
elif len(best_teas) == 1:
    print(f" -> Most stock: {best_teas[0]} ({best_qty}g)")
else:
    print(f" -> Tied for most stock: {', '.join(best_teas)} ({best_qty}g)")