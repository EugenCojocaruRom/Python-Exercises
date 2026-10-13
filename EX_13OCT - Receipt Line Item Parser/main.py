#Print header and separator
print("<-- Receipt Line Item Parser -->")
print("--------------------------------")

#Set constants for big line limit, discount threshold and discount rate
BIG_LINE_LIMIT = 5
DISCOUNT_THRESHOLD = 15.00
DISCOUNT_MULTIPLIER = 0.90

#Have a list of raw data
raw_lines = [
    "  apple , 3 , 0.35 ",
    "BREAD,1,2.25",
    " milk ,2, 0.90",
    "apple,2,0.50",
    "Cheese , 1 , 4.80 ",
    "bread, 2, 1.35",
    "",
    "banana,4,1.75",
]

#Create empty list for storing the items
items = []
#Loop over the raw_lines list
for line in raw_lines:
    #Skip the line if it is empty
    if line.strip() == "":
        continue
    #Split the line on commas -> results in a list of 3 strings
    parts = line.split(",")
    #Unpack the parts into three variables, cleaned with strip()
    name = parts[0].strip().lower() #strip spaces + lowercase
    quantity = int(parts[1].strip()) #strip spaces + convert to int
    price = float(parts[2].strip()) #strip spaces + convert to float
    #Add the tuple (name, quantity, price) to the items list
    items.append((name, quantity, price))

#Create empty dictionary to store the total quantity per item
quantities = {}
#Create empty dictionary to store the total money per item
line_totals = {}
#Loop over the items list
for name, quantity, price in items:
    #Add the quantity to the running total for this item
    quantities[name] = quantities.get(name, 0) + quantity
    #Add the price per line to the running total for this item
    line_totals[name] = line_totals.get(name, 0) + quantity * price

#Print a numbered report
print("=== Receipt Report ===")
#Loop with enumerate(), starting at 1, over the item names sorted alphabetically
for number, name in enumerate(sorted(quantities), start = 1):
    #Get the total quantity and the unit price for this item
    qty = quantities[name]
    #Calculate the line total
    line_total = line_totals[name]
    #Calculate the unit price (average of line total divided by quantity)
    unit_price = line_total / qty
    #Print the aligned, formatted row
    print(f"{number}. {name:<8} x{qty:<3} @ ${unit_price:.2f} = ${line_total:.2f}")

#Calculate the grand total as the sum of the line_totals dictionary's values
grand_total = sum(line_totals.values())
#Find the most expensive line(s)
top_amount = max(line_totals.values())
top_names = [name for name, amount in line_totals.items() if amount == top_amount]
#Get the number of unique items
unique_count = len(line_totals)

#Print the header and the summary elements
print("\n=== Summary ===")
print(f"Grand total: ${grand_total:.2f}")
if len(top_names) == 1:
    print(f"Most expensive line: {', '.join(top_names)} (${top_amount:.2f})")
else:
    print(f"Most expensive lines: {', '.join(top_names)} (${top_amount:.2f})")
print(f"Unique items: {unique_count}")

#Filter the names whose line total is greater than the limit set by the user
big_lines = [name for name, amount in line_totals.items() if amount > BIG_LINE_LIMIT]
#Print the lines over the limit
print(f"\n=== Lines over ${BIG_LINE_LIMIT:.2f} ===")
if len(big_lines) == 0:
    print(f" No lines over ${BIG_LINE_LIMIT:.2f}")
elif len(big_lines) == 1:
    print(f" Only 1 line: {', '.join(big_lines)}")
else:
    print(f" Multiple lines: {', '.join(big_lines)}")

#Apply the discount to totals over the threshold
if grand_total > DISCOUNT_THRESHOLD:
    #Keep 90% of the total (grand_total * 0.9)
    discounted_total = grand_total * DISCOUNT_MULTIPLIER
    print(f"\nOriginal total: ${grand_total:.2f}")
    print(f"Discounted total: ${discounted_total:.2f}")
else:
    print(f"Total: ${grand_total:.2f}")