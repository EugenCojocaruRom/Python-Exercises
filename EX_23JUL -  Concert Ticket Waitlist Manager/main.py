#Print header and separator
print("<-- Concert Ticket Waitlist Manager -->")
print("---------------------------------------")

#Prompt user to enter the number of buyers
num_buyers = int(input("Enter number of buyers: "))
#Create empty list to hold the names of the buyers and the number of tickets requested
waitlist = []
#Loop over the number of buyers
for i in range(num_buyers):
    #Prompt user to enter the name of the buyer
    name = input(f"Enter name of buyer {i + 1}: ").strip().title()
    #Prompt user to enter the number of tickets
    number_of_tickets_requested = int(input(f"How many tickets for {name}? "))
    #Add name and number of tickets to waitlist
    waitlist.append((name, number_of_tickets_requested))

print()
#Loop over the waitlist
for i, (name, number_of_tickets_requested) in enumerate(waitlist, start = 1):
    #Set condition for only 1 ticket
    if number_of_tickets_requested == 1:
        print(f"Position {i}. {name} - {number_of_tickets_requested} ticket")
    #Set condition for several tickets
    else:
        print(f"Position {i}. {name} - {number_of_tickets_requested} tickets")

#Calculate the total number of tickets
total_tickets = sum(number_of_tickets_requested for (name, number_of_tickets_requested) in waitlist)
#Print the total number of requested tickets
print(f"\nTotal number of tickets: {total_tickets}")

#Prompt user to enter the number of available tickets
available_tickets = int(input("\nHow many tickets are available? "))

#Establish who gets tickets
tickets_remaining = available_tickets
for name, number_of_tickets_requested in waitlist:
    if number_of_tickets_requested > tickets_remaining:
        print(f"Not enough tickets available for {name}.")
        continue
    else:
        tickets_remaining = tickets_remaining - number_of_tickets_requested
        if number_of_tickets_requested == 1:
            print(f"{name} got {number_of_tickets_requested} ticket.\n  Remaining tickets: {tickets_remaining}")
        else:
            print(f"{name} got {number_of_tickets_requested} tickets.\n  Remaining tickets: {tickets_remaining}")

print()
#Find the buyers that requested more than 2 tickets
big_buyers = [name for (name, number_of_tickets_requested) in waitlist if number_of_tickets_requested > 2]
#Print the list
if len(big_buyers) == 0:
    print("Nobody wanted to buy more than 2 tickets.")
else:
    print(f"The following people wanted to buy more than 2 tickets: {', '.join(big_buyers)}.")

print()
#Print the remaining tickets
if tickets_remaining == 0:
    print("All the tickets have been sold! Nicely done! 🎉")
else:
    if tickets_remaining == 1:
        print(f"There is still {tickets_remaining} ticket available.")
    else:
        print(f"There are still {tickets_remaining} tickets available.")