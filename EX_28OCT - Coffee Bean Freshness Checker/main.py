#Print header and separator
print("<== Coffee Bean Freshness Checker ==>\n-------------------------------------")

#Define function
def get_status(days):
    if days <= 7:
        return "Fresh"
    elif days <= 20:
        return "Good"
    elif days <= 30:
        return "Use soon"
    else:
        return "Expired"

#Create empty list to store the coffe origins and number of days since roasting
bags = []
#Prompt user to enter a number of coffee types in the store
while True:
    try:
        num_coffe_types = int(input("Enter the number of coffee types in the store: "))
        if num_coffe_types <= 0:
            print("The number of coffee types cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of coffee types
for i in range(num_coffe_types):
    #Loop for validating the coffee origin
    while True:
        #Prompt user to enter the origin of the coffee
        origin = input(f"Enter origin for coffee {i + 1}: ").strip().title()
        #Check that the coffee origin entered is not empty
        if origin == "":
            print("The origin cannot be empty. Please try again.")
            continue
        if not origin.replace(" ", "").replace("-", "").isalpha():
            print("The origin can only contain letters, spaces, and hyphens. Please try again.")
            continue
        break
    #Loop for validating the days since roasting the coffee
    while True:
        try:
            #Prompt user to enter the days since roasting the coffee
            days_since_roasting = int(input(f"Enter the number of days since roasting the {origin} coffee: "))
            # Check that the number of days is not negative
            if days_since_roasting < 0:
                print("The number of days must be at least 0. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add origin and number of days to the bags list
    bags.append((origin, days_since_roasting))

print()
#Loop through the bags list and print all the coffees
for i, (origin, days_since_roasting) in enumerate(bags, 1):
    print(f"{i}. {origin} - {days_since_roasting} - {get_status(days_since_roasting)}")

print()
#Filter the origins by status "expired"
expired_cofee = [origin for origin, days_since_roasting in bags if get_status(days_since_roasting) == "Expired"]
if not expired_cofee:
    print("There is no expired coffee in the shop.")
elif len(expired_cofee) == 1:
    print(f"The {expired_cofee[0]} coffee is expired. Throw it away!")
else:
    print(f"The following coffee types are expired and must be thrown away: {', '.join(expired_cofee)}")

#Filter the origins by status “Fresh” or “Good”
good_cofee = [origin for origin, days in bags
              if get_status(days ) in ("Fresh", "Good")]
if not good_cofee:
    print("The coffee in the shop is either expired or about to. Get some fresh beans for roasting!")
else:
    print(f"Ready to serve: {', '.join(good_cofee)}")

print()
#Calculate the average age of all the bags
avg_age = sum(days_since_roasting for _, days_since_roasting in bags) / len(bags)
print(f"Average age: {avg_age:.1f} days")

#Find and print the oldest bag + how many days old it is
most_days = max(bags, key=lambda bag: bag[1])
#Create a list with the bags that match the highest number of days
oldest_bag = [origin for origin, days_since_roasting in bags if days_since_roasting == most_days]
#Set conditions for displaying the oldest bags
if len(oldest_bag) == 1:
    print(f"Oldest bag: {oldest_bag[0]} ({most_days} days)")
else:
    print(f"Oldest bags: {', '.join(oldest_bag)} ({most_days} days)")
