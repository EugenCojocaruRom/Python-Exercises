#Print header and separator
print("<-- Water Bottle Refill Tracker -->")
print("-----------------------------------")

#Create function for asking a positive number
def ask_positive_number(prompt, as_int=False):
    while True:
        try:
            value = int(input(prompt)) if as_int else float(input(prompt))
            if value <= 0:
                print("The value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a correct value.")

#Create empty list to store the bottle quantities
bottles = []
#Prompt user to enter a number of bottles
num_bottles = ask_positive_number("Enter the number of bottles of water for the day: ", as_int=True)
#Loop over the number of bottles
for i in range(num_bottles):
    #Prompt user to enter the water quantity in the bottle
    quantity = ask_positive_number(f"Enter the quantity for bottle {i + 1}: ", as_int = True)
    #Add the quantity to the bottles list
    bottles.append(quantity)

#Print header
print("\n == List of bottles for the day ==")
#Enumerate and print all the bottles for the day
for i, bottle in enumerate(bottles, start = 1):
    print(f"Bottle {i}: {bottle} ml")

#Calculate the total quantity
total_quantity = sum(bottles)
#Convert into liters
liters = total_quantity / 1000
#Print the total quantity in liters
print(f"\nTotal quantity for the day: {liters:.2f} liters")

#Print empty line
print()
#Find and print a list of large bottles (at least 500 ml)
large_bottles = [quantity for quantity in bottles if quantity >= 500]
if not large_bottles:
    print("No bottles of at least 500 ml.")
elif len(large_bottles) == 1:
    print(f"Only one bottle of at least 500 ml found: {large_bottles[0]}")
else:
    large_text = ", ".join(str(b) for b in large_bottles)
    print(f"There are {len(large_bottles)} bottles of at least 500 ml: {large_text}")

#Print the number of bottle smaller than 500 ml
print(f"Bottles smaller than 500 ml: {len(bottles) - len(large_bottles)}")

#Prompt user to enter the daily goal
goal = ask_positive_number("\nEnter the goal for the day (liters): ")
#Check that the daily goal has been met
goal_ml = round(goal * 1000)
missing_qty = goal_ml - total_quantity
if total_quantity > goal_ml:
    print(f"Nice job! You went over your goal of {goal} liters by {total_quantity - goal_ml} ml!")
elif total_quantity == goal_ml:
    print(f"Your goal of {goal} liters has been reached! Congratulations!")
else:
    print(f"You still need {missing_qty:.0f} ml to reach your goal. Keep hydrating!")