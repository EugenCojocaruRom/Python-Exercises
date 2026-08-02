#Print header and separator
print("<-- Ski Resort Lift Ticket Tracker -->")
print("--------------------------------------")

#Create empty list to store the customer name, the ticket type and the price
tickets = []
#Initiate loop to allow the user to enter customer name, ticket type and price
while True:
    #Prompt user to enter the customer's name
    customer_name = input("Enter customer name (or 'done' to finish): ").strip().title()
    if customer_name.lower() == "done":
        break
    #Prompt user to enter a ticket type
    while True:
        try:
            ticket_type = input(f"Enter ticket type for {customer_name}: ").strip().title()
            break
        except ValueError:
            print("Please enter a valid ticket type.")
    #Loop for validating the ticket price
    while True:
        try:
            #Prompt user to enter the ticket price
            price = float(input(f"Enter the price for the {ticket_type} ticket: $"))
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, ticket type and price to the tickets list
    tickets.append((customer_name, ticket_type, price))

#Print header
print("\n<-- TICKETS -->")
#Loop over the tickets list
for i, (customer_name, ticket_type, price) in enumerate(tickets, start = 1):
    #Print customer name, ticket type and price
    print(f"{i}: {customer_name} -> {ticket_type} - ${price}")

#Calculate and print the total revenue for the day
daily_revenue = [price for customer_name, ticket_type, price in tickets]
print(f"\nTotal revenue for today: ${sum(daily_revenue):.2f} ({len(daily_revenue)} tickets sold)")

print()
#Find and print the number of 'season pass' tickets
season_pass = [ticket_type for customer_name, ticket_type, price in tickets if ticket_type.lower() == "season pass"]
if len(season_pass) == 0:
    print("No Season Passes have been sold today.")
else:
    if len(season_pass) == 1:
        print(f"We sold {len(season_pass)} Season Pass today.")
    else:
        print(f"We sold {len(season_pass)} Season Passes today.")

#Find the highest-priced sale
print()
try:
    top_name, top_ticket, top_price = max(tickets, key = lambda x: x[2])
    high_price = [(name, ticket_type, price) for name, ticket_type, price in tickets if price == top_price]
    if len(high_price) != 1:
        print(f"There are {len(high_price)} high-priced sales:")
    for name, ticket_type, price in high_price:
        if len(high_price) == 1:
            print(f"The highest-priced sale: {name} - {ticket_type} (${price})")
        else:
            print(f"  {name} - {ticket_type} (${price})")
except ValueError:
    print("We made no sales today :-(")

#Create empty dictionary for the total revenue per ticket type
revenue_per_ticket = {}
#Loop over the tickets list
for customer_name, ticket_type, price in tickets:
    #Set condition for ticket type already in the dictionary
    if ticket_type in revenue_per_ticket:
        #Increment the revenue per ticket by the corresponding price
        revenue_per_ticket[ticket_type] += price
    #Set condition for ticket type not in the dictionary
    else:
        #Set the revenue per ticket as the corresponding price
        revenue_per_ticket[ticket_type] = price
#Sort and print the ticket types ordered by total revenue
sorted_revenue = sorted(revenue_per_ticket.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Revenue per Ticket Type -->")
for i, (ticket_type, total) in enumerate(sorted_revenue, start = 1):
    print(f"{i}. {ticket_type}: ${total}")