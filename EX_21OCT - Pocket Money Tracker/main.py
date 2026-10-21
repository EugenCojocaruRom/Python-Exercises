#Print header and separator
print("<-- Pocket Money Tracker -->")
print("----------------------------")

#Prompt user to enter the weekly budget
budget = float(input("Enter the weekly budget ($): "))
#Have list with days, categories and amounts
expenses = [
    ("Mon", "food", 12.50),
    ("Mon", "transport", 3.00),
    ("Tue", "food", 8.75),
    ("Wed", "fun", 15.00),
    ("Wed", "food", 10.25),
    ("Thu", "transport", 3.00),
    ("Fri", "fun", 22.50),
    ("Sat", "food", 18.00),
    ("Sun", "fun", 32.70),
    ("Sun", "transport", 5.17)
]

#Print all the expense, in a numbered format
for i, (day, category, amount) in enumerate(expenses, start = 1):
    print(f"{i}. {day} - {category}: ${amount:.2f}")

#Calculate and print the total spent
total_expenses = sum(amount for day, category, amount in expenses)
print(f" -> Total spent: ${total_expenses:.2f}")
if total_expenses > budget:
    print(f"You are over budget by ${(total_expenses - budget):.2f}!")
else:
    print("You are within budget.")

#Calculate the amount spent on food only
food_expenses = sum(amount for day, category, amount in expenses if category == "food")
print(f" -> Total spent on food: ${food_expenses:.2f}")

#Check that the expenses list has values to guard against errors
if expenses:
    #Calculate the average spent per expense
    average_expense = total_expenses / len(expenses)
    print(f" -> Average per expense: ${average_expense:.2f}")
else:
    print("No expenses recorded, so no average.")

#Check that the expenses list has values to guard against errors
if expenses:
    #Find the largest expense
    largest_expense = max(expenses, key = lambda expense: expense[2])
    day, category, amount = largest_expense
    print(f"\nThe largest expense: {day} - {category}: ${amount:.2f}")
else:
    print("No expenses recorded, so no largest expense.")

#Print header
print("\n== Big Spender Days ==")
#Prompt user to enter a spending limit
spending_limit = float(input("Enter the spending limit ($): "))
#Find the days when expenses were over the set spending limit
big_spender_days = [(day, category, amount) for day, category, amount in expenses if amount > spending_limit]
#Set conditions for displaying the big spender days
if not big_spender_days:
    print(f"No amounts over ${spending_limit:.2f}.")
elif len(big_spender_days) == 1:
    day, category, amount = big_spender_days[0]
    print(f"You went over the ${spending_limit:.2f} limit only once: {day} - {category}: ${amount:.2f}")
else:
    if len(big_spender_days) == 2:
        print(f"You went over the ${spending_limit:.2f} limit twice:")
    else:
        print(f"You went over the ${spending_limit:.2f} limit {len(big_spender_days)} times:")
    #Loop over the big spender days list
    for day, category, amount in big_spender_days:
        print(f" {day} - {category}: ${amount:.2f}")