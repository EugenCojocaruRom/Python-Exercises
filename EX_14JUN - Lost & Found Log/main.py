#Prompt the user to enter the number of items found
num_items = int(input("Enter the number of items in the box: "))
#Create empty list to hold the items, days and claiming status
box = []
#Loop through the number of items
for i in range(num_items):
    #Prompt user to enter the name of the item
    item_name = input(f"Enter name of item {i + 1}: ").strip().capitalize()
    #Prompt user to enter the number of days the object has been in the box
    days_in_box = int(input("How many days has it been in the box? "))
    #Prompt user to enter the claiming status
    claimed = input("Has this item been claimed? (Yes/No) ").strip().capitalize()
    #Set condition to add true/false to the tuple depending on the claiming status
    if claimed == "Yes":
        claimed = True
    else:
        claimed = False
    #Add the tuple to the list
    box.append((item_name, days_in_box, claimed))

#Print box contents
print("\nObjects in the Lost & Found Box:")
#Loop through the box list
for j, (item_name, days_in_box, claimed) in enumerate(box, start = 1):
    #Print each item
    print(f"{j}. {item_name} | Days in the box: {days_in_box} | Claimed: {'Yes' if claimed else 'No'}")

#Filter the items that have been in the box for more than 3 days
unclaimed_items = [(item, days_in_box, claimed) for item, days_in_box, claimed in box if not claimed and days_in_box > 3]
#Print section title
print("\nThe following items have been in the box for more than 3 days:")
for (item_name, days_in_box, claimed) in unclaimed_items:
    print(f" -> {item_name} - {days_in_box} days")

#Print section title
print("\nThis object has been in the box the longest:")
#Find the item that has been in the box the longest (claimed or not)
veteran_item = max(box, key=lambda x: x[1])
#Unpack the item into name, days and claimed status
name, days, claimed = veteran_item
#Print the item
print(f"  {name} - {days} days")

#Declare variable for storing the claimed items
claimed_items = 0
for (item_name, days_in_box, claimed) in box:
    if claimed:
        claimed_items += 1
#Print the number of claimed items
print(f"\nThere are {claimed_items} items in the box that have been claimed.")

#Print section title
print("\n<-- Summary -->")
#Print the summary of the box
print(f"There are {len(box)} items in the box, out of which:")
print(f"  -> {claimed_items} have been claimed")
print(f"  -> {len(unclaimed_items)} are unclaimed (in the box for over 3 days)")
#Unpack the veteran item into name, days and claimed status
name, days, claimed = veteran_item
print(f"  -> {name} has been in the box the longest ({days} days)")
