#Print header and separator
print("<-- Car Wash Service Queue Tracker -->")
print("--------------------------------------")

print("Welcome to out car wash!")
print("Available wash types:"
      "\n Basic: $10"
      "\n Deluxe: $20"
      "\n Premium: $35")

#Create list of tuples for the cars wash programs
wash_programs = [("Basic", 10), ("Deluxe", 20), ("Premium", 35)]

#Create list of just the valid wash type names, for easy checking
valid_wash_names = [name for name, price in wash_programs]

print()
#Create empty list to store the license plate and the wash type
cars = []
#Initiate loop to allow the user to enter the license plate and the wash type
while True:
    #Prompt user to enter the license plate
    plate = input(f"Enter the license plate number (format XXX123) or 'done' to finish: ").strip().upper()
    #Check for the exit condition first before validating the license plate format
    if plate.lower() == "done":
        break
    #Set conditions to check the license plate length, the existence of 3 letters and 3 digits
    if len(plate) == 6 and plate[:3].isalpha() and plate[3:6].isdigit():
        while True:
            # Prompt user to enter the wash type
            wash_type = input(f"Enter the wash type for {plate}: ").strip().title()
            # Check that it matches one of the actual program names
            if wash_type in valid_wash_names:
                break
            print(f"Please enter a valid wash type ({', '.join(valid_wash_names)}).")
        #Look up the price for this wash type from wash_programs
        price = next(p for name, p in wash_programs if name == wash_type)
        #Add license plate and wash type to the cars list
        cars.append((plate, wash_type, price))
    else:
        #Print informative message and prompt for a new attempt
        print("Invalid license plate number, please try again.")

#Apply a 10% loyalty discount to repeated plates (2nd+ wash), as a separate pass
plate_seen_count = {}
discounted_cars = []
#Loop over the cars list
for plate, wash_type, price in cars:
    #Track how many times this plate has been seen so far (including this one)
    plate_seen_count[plate] = plate_seen_count.get(plate, 0) + 1
    #If this is the 2nd or later wash for this plate, apply 10% discount
    if plate_seen_count[plate] > 1:
        discounted_price = round(price * 0.9, 2)
    else:
        discounted_price = price
    discounted_cars.append((plate, wash_type, discounted_price))

#Print header
print("\n<-- CAR WASH QUEUE -->")
#Loop over the cars list
for i, (plate, wash_type, price) in enumerate(cars, start = 1):
    #Print license plate, wash type and price
    print(f"{i}: {plate} - {wash_type} - ${price}")

#Calculate and print the total revenue (for all the cars)
total_revenue = sum(price for plate, wash_type, price in cars)
print(f"  Total revenue: ${total_revenue}")

#Print the discounted queue
print("\n<-- CAR WASH QUEUE (with loyalty discount) -->")
for i, (plate, wash_type, discounted_price) in enumerate(discounted_cars, start=1):
    print(f"{i}: {plate} - {wash_type} - ${discounted_price:.2f}")

#Recalculate total revenue using the discounted prices
discounted_revenue = sum(price for plate, wash_type, price in discounted_cars)
print(f"  Total revenue after loyalty discounts: ${discounted_revenue:.2f}")
print(f"    (Original total revenue was: ${total_revenue})")

#Find and print only the 'premium' programs requested
print("\n<-- PREMIUM WASH QUEUE -->")
#Filter the premium  washes
premium_wash = [plate for plate, wash_type, price in cars if wash_type == "Premium"]
#Loop over the premium wash list
if len(premium_wash) == 0:
    print('No "Premium" wash programs found.')
else:
    if len(premium_wash) == 1:
        print(f"Only 1 premium wash program found: {premium_wash[0]}")
    else:
         print(f"There were {len(premium_wash)} premium wash programs: {', '.join(premium_wash)}")

#Create empty dictionary to count how many times each wash type occurs
wash_type_counts = {}
for plate, wash_type, price in cars:
    wash_type_counts[wash_type] = wash_type_counts.get(wash_type, 0) + 1
#Find the most common wash type
top_wash_type = max(wash_type_counts, key=wash_type_counts.get)
print(f'\nThe most common wash type is "{top_wash_type}" ({wash_type_counts[top_wash_type]} washes).')

#