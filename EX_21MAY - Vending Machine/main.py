#Prompt user for number of items
num_items = int(input("Enter the number of items in the vending machine: "))

#Declare empty dictionary for storing the items and the prices
items = {}
#Loop through the number of items
for i in range(num_items):
    #Prompt user for item name
    item_name = input(f"Enter item {i + 1}: ")
    #Prompt user for item price
    item_price = float(input(f"Enter price for item {i + 1}: "))
    #Add item and price to dictionary
    items[item_name] = item_price
#Print list of items
print("The following items are available: ")
for i, (name, price) in enumerate(items.items(), start=1):
    print(f"{i}. {name:<10} ${price:.2f}")

#Declare variable for balance
balance = 0.0
#Loop for as long as the condition is true
while True:
    #Prompt user to insert coin
    coin = float(input("Insert a coin (e.g. 5, 10, 25, 50): ")) / 100
    #Update the balance and round it to 2 decimals
    balance = round(balance + coin, 2)
    #Filter the affordable items
    affordable_items = [item for item in items if items[item] <= balance]
    #Set condition for balance bigger than the cheapest item
    if affordable_items:
        #Print message
        print(f"You can buy: {', '.join(affordable_items)}")
        #Prompt user to insert additional coins or stop
        add_coins = input("Do you want to add another coin? (Y/N): ")
        #Set condition for negative answer
        if add_coins.upper() == "N":
            #End the loop
            break
    #Set condition for balance smaller than the cheapest item
    else:
        print(f"You don't have enough money!")

#Loop for as long as the condition is true
while True:
    #Print the available items
    print("\nThe following items are available: ")
    for i, (name, price) in enumerate(items.items(), start=1):
        print(f"{i}. {name:<10} ${price:.2f}")
    #Print the balance
    print(f"Balance: ${balance:.2f}")
    #Prompt user to make a selection
    selected_item = int(input("Select an item: "))
    #Assign a key to the item based on the user input
    item_names = list(items.keys())
    #Identify the item based on the key
    chosen_item = item_names[selected_item - 1]
    #Look for the corresponding price
    sel_item_price = items[chosen_item]
    #Set condition for price smaller than balance
    if sel_item_price <= balance:
        #Calculate the change to return
        change = balance - sel_item_price
        #Print message
        print(f"Here's your {chosen_item}! Change: ${change:.2f}")
        #Exit the loop when the purchase is successful
        break
    else:
        #Calculate the amount due
        amount_due = sel_item_price - balance
        #Print message
        print(f"Not enough money! You still need ${amount_due:.2f}")
        #Loop to add more coins
        while True:
            #Prompt user to insert coin
            coin = float(input("Insert a coin (e.g. 5, 10, 25, 50): ")) / 100
            #Update the balance and round it to 2 decimals
            balance = round(balance + coin, 2)
            #Print the balance
            print(f"Balance: ${balance:.2f}")
            #Set condition for balance bigger than the selected item price
            if balance >= sel_item_price:
                #End the loop
                break
            #Prompt user to insert additional coins or stop
            add_coins = input("Do you want to add another coin? (Y/N): ")
            #Set condition for negative answer
            if add_coins.upper() == "N":
                #End the loop
                break