#Print header and separator
print("<-- Hotel Minibar Billing Report -->")
print("------------------------------------")

#Have a dictionary of items and prices
prices = {
    "water": 2.50,
    "cola": 3.00,
    "chips": 4.50,
    "chocolate": 3.75,
    "beer": 5.00,
    "wine": 12.00,
    "pickles": 8.00
}

#Have a list with the room number and item taken from the minibar -> (room_number, item) – one entry per item taken
log = [
    (101, "water"), (102, "beer"), (101, "chips"), (103, "cola"),
    (102, "beer"), (101, "water"), (103, "wine"), (102, "chocolate"),
    (101, "cola"), (103, "juice"), (102, "water"), (103, "chips"),
    (104, "pickles"), (104, "beer"), (104, "chips"), (104, "cola"),
    (102, "pickles"), (104, "juice"), (104, "water"), (101, "beer")
]

#Group the items by room number
items_by_room = {}
#Loop over the log list
for room_number, item in log:
    #Set condition for the room number not in the dictionary
    if room_number not in items_by_room:
        #This room is seen for the first time
        items_by_room[room_number] = []
    #Add the item to the room's list
    items_by_room[room_number].append(item)

#Create empty dictionary to store the number of items across all rooms
item_counts = {}
#Loop over the log list
for room_number, item in log:
    #Set condition for checking if the item is in the prices dictionary
    if item in prices:
        #Count the items
        item_counts[item] = item_counts.get(item, 0) + 1

#Create empty list to store the unknown items
unknown_items = []
#Create empty dictionary to store the final bills per room
final_bills = {}
#Loop over the sorted dictionary of items per room
for room_number in sorted(items_by_room):
    #Count the items per room
    items = items_by_room[room_number]
    #Create empty dictionary to store the room number and the item counts
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    #Declare variable for storing the room total and initialize it
    room_total = 0
    #Declare variable for storing the billable items and initialize it
    billable_items = 0
    #Calculate the room total
    for item, quantity in counts.items():
        #Check that the item has a corresponding price in the prices dictionary
        if item in prices:
            #Increase room total by multiplying the price of the item with the item quantity
            room_total += quantity * prices[item]
            #Increase the billable item count by the quantity value
            billable_items += quantity
        #Set condition for handling unknown items (not in the prices dictionary)
        else:
            #Check that the item is not already in the unknown items list
            if item not in unknown_items:
                #Add the item to the unknown items list
                unknown_items.append(item)
    #Declare variable for the service fee and initialize it
    service_fee = 0
    #Set condition for billable items >= a certain number (e.g. >= 4)
    if billable_items >= 4:
        service_fee = 5.00
    #Add the service fee to the room total
    room_total += service_fee #Which can be 0 or 5, depending on the number of items taken
    #Declare variable for discounted total and initialize it as the room total
    discounted_total = room_total
    #Set condition for room total >= 20
    if room_total >= 20:
        discounted_total = round(room_total * 0.9, 2)
    #Add the discounted total to the final bills dictionary
    final_bills[room_number] = discounted_total
    #Filter the items and the amounts
    parts = [f"{quantity} x {item}" for item, quantity in counts.items()]
    #Print the report per room
    room_report = f"Room {room_number}: {', '.join(parts)} -> ${room_total:.2f}"
    #Set condition for printing the extra service fee if applicable
    if service_fee > 0:
        #Add the service fee to the room report
        room_report += f"\n        | includes service fee of ${service_fee:.2f}"
    #Set condition for printing the discounted total as well
    if discounted_total < room_total:
        #Add the extra info to the room report
        room_report += f"\n        | with 10% discount: ${discounted_total:.2f}"
    #Print the room report
    print(room_report)
#Handle unknown items
if unknown_items:
    print(f"\nItems not in the price list: {', '.join(unknown_items)}")

print()
#Loop over the rooms
for i, (room_number, final_total) in enumerate(sorted(final_bills.items()), start=1):
    print(f"{i}. Room {room_number}: ${final_total:.2f}")
# Total revenue (including discounts)
total_revenue = sum(final_bills.values())
#Find the highest bill
top_room = max(final_bills, key = final_bills.get)
#Find the highest item count
max_count = max(item_counts.values())
#Collect all the items that have that count
top_items = [item for item, count in item_counts.items() if count == max_count]
tied_top_items = [f"{max_count} x {item}" for item in top_items]

#Print the summary
print("\n<== MINIBAR BILLING SUMMARY ==>")
print(f"Total revenue: ${total_revenue:.2f}")
print(f"Highest bill: Room {top_room} (${final_bills[top_room]:.2f})")
print(f"Most popular item(s): {', '.join(tied_top_items)}")

