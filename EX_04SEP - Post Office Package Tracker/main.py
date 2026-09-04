#Print header and separator
print("<-- Post Office Package Tracker -->")
print("-----------------------------------")

#Create empty list to store the senders' names and packages weights as tuples
packages = []
#Declare variable for package base fee
base_fee = 2
#Prompt user to enter a number of packages processed today
while True:
    try:
        num_packages = int(input("Enter the number of packages being processed today: "))
        if num_packages <= 0:
            print("The number of packages cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of packages
for i in range(num_packages):
    #Loop for validating the sender's name
    while True:
        #Prompt user to enter the sender's name
        sender = input(f"Enter the name of sender {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if sender == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not sender.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the package weight
    while True:
        try:
            #Prompt user to enter the package weight
            weight = float(input(f"Enter the weight of {sender}'s package (in kg): "))
            #Check that the duration value is positive
            if weight <= 0:
                print("The weight must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Calculate the cost per package (including surcharge for heavy packages -> €0.75 per kg over 5kg)
    if weight > 5:
        shipping_fee = base_fee * weight + ((weight - 5) * 0.75)
    else:
        shipping_fee = base_fee * weight
    #Add the sender's name, package weight and shipping fee to the packages list
    packages.append((sender, weight, shipping_fee))

#Print header
print("\n<-- PACKAGES SENT TODAY -->")
#Loop over the packages list
for i, (sender, weight, shipping_fee) in enumerate(packages, start = 1):
    #Create variable 'tag' to display 'heavy package' for packages over 5 kg
    tag = " (heavy package)" if weight > 5 else ""
    #Print the sender's name, the package weight and the shipping fee
    print(f" {i}. {sender} - {weight:.3f} kg - €{shipping_fee:.2f}{tag}")

#Calculate and print the total weight for all the packages as well as the average weight
total_weight = sum(weight for sender, weight, shipping_fee in packages)
avg_weight = total_weight / num_packages
print(f"  Total weight of all packages: {total_weight:.3f} kg")
print(f"  Average weight of packages: {avg_weight:.3f} kg")

#Print header
print("\n<-- HEAVY PACKAGES (> 5 KILOS) -->")
#Find and print all packages heavier than 5 kilos
heavy_packages = [(sender, weight, shipping_fee) for sender, weight, shipping_fee in packages if weight > 5]
if len(heavy_packages) == 0:
    print("There was no heavy package.")
elif len(heavy_packages) == 1:
    print(f"There was only 1 heavy package:")
else:
    print(f"There were {len(heavy_packages)} heavy packages:")
# Print the packages once, regardless of which branch ran above
for sender, weight, shipping_fee in heavy_packages:
    print(f" {sender} - {weight:.3f} kg")

#Find the heaviest package
print()
top_weight = max(packages, key=lambda x: x[1])[1]
top_heavy_packs = [(sender, weight) for sender, weight, shipping_fee in packages if weight == top_weight]
if len(top_heavy_packs) == 1:
    top_sender, top_weight = top_heavy_packs[0]
    print(f"The heaviest package was sent by {top_sender} ({top_weight:.3f} kg).")
else:
    names = ', '.join(f"{sender_name} ({pack_weight} kg)" for sender_name, pack_weight in top_heavy_packs)
    print(f"The heaviest packages ({top_weight:.3f} kg) were sent by: {names}.")

#Calculate the total shipping revenue for all packages
total_revenue = sum(shipping_fee for sender, weight, shipping_fee in packages)
print(f"\nTotal shipping revenue collected for all packages: €{total_revenue:.2f}")